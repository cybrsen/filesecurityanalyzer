import os
import re
import logging
import pandas as pd
from docx import Document
import pdfplumber
from datetime import datetime

# Configure logging with date in filename
log_directory = r'/path/to/your/directory'
os.makedirs(log_directory, exist_ok=True)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f'file_scan_{current_time}.log'
logging.basicConfig(filename=os.path.join(log_directory, log_filename), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

def read_txt(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def read_docx(filepath):
    doc = Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def read_pdf(filepath):
    with pdfplumber.open(filepath) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])

def read_xlsx(filepath):
    df = pd.read_excel(filepath)
    df = df.astype(str).replace('nan', '')
    return "\n".join(df.apply(lambda row: ' '.join(row.values), axis=1))

def scan_files(directory):
    results = []
    patterns = {
        'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        'social_security_number': r'\b\d{3}-?\d{2}-?\d{4}\b',
        'credit_card_number': r'\b(?:\d{4}[- ]?){3}\d{4}\b',
        'phone_number': r'\b(?:\+1[-.\s]?)?(?:\(\d{3}\)[-.\s]?|\d{3}[-.\s]?)(?:\d{3}[-.\s]?\d{4})\b',
        'date_of_birth': r'\b(?:0?[1-9]|1[0-2])[-/.](?:0?[1-9]|[12]\d|3[01])[-/.](?:19|20\d{2})\b'
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            content = ""
            try:
                file_stat = os.stat(filepath)
                file_perms = oct(file_stat.st_mode)[-3:]
                if int(file_perms, 8) > 0o644:
                    logging.warning(f"{filepath} has permissive settings: {file_perms}")
            except Exception as e:
                logging.error(f"Error checking permissions for {filepath}: {str(e)}")
                continue

            if filepath.endswith('.txt'):
                content = read_txt(filepath)
            elif filepath.endswith('.docx'):
                content = read_docx(filepath)
            elif filepath.endswith('.pdf'):
                content = read_pdf(filepath)
            elif filepath.endswith('.xlsx'):
                if file.startswith('~$'):
                    logging.warning(f"Skipping temporary or locked file: {filepath}")
                    continue
                try:
                    content = read_xlsx(filepath)
                except Exception as e:
                    logging.error(f"Error reading {filepath}: {str(e)}")
                    continue
            else:
                continue

            try:
                file_results = {}
                for type, pattern in patterns.items():
                    matches = re.findall(pattern, content)
                    if matches:
                        file_results[type] = len(matches)
                if file_results:
                    results.append((filepath, file_results))
            except Exception as e:
                logging.error(f"Failed to process {filepath}: {str(e)}")

    for result in results:
        filepath, data = result
        logging.info(f"Results for {os.path.basename(filepath)}:")
        for info_type, count in data.items():
            logging.info(f"Found {count} {info_type}(s)")

# Example usage
directory_to_scan = r'/path/to/your/directory'
scan_files(directory_to_scan)


