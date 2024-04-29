import os
import re
import logging
import pandas as pd
from docx import Document
import pdfplumber

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_txt(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def read_docx(filepath):
    doc = Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def read_pdf(filepath):
    with pdfplumber.open(filepath) as pdf:
        return "\n".join([page.extract_text() or "" for page in pdf.pages])  # Handle None results from extract_text

def read_xlsx(filepath):
    df = pd.read_excel(filepath)
    df = df.astype(str).fillna('')  # Convert all entries to string and fill NaNs
    return "\n".join(df.sum(axis=1))  # Concatenate all cells into a single string for each row and join rows

def scan_files(directory):
    results = []
    patterns = {
        'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        'social_security_number': r'\b\d{3}-\d{2}-\d{4}\b',
        'credit_card_number': r'\b(?:\d{4}[- ]?){3}\d{4}\b',
        'phone_number': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'date_of_birth': r'\b(?:0[1-9]|1[0-2])[-/.](?:0[1-9]|[12][0-9]|3[01])[-/.](?:19|20)\d{2}\b'
    }

    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            content = ""
            if filepath.endswith('.txt'):
                content = read_txt(filepath)
            elif filepath.endswith('.docx'):
                content = read_docx(filepath)
            elif filepath.endswith('.pdf'):
                content = read_pdf(filepath)
            elif filepath.endswith('.xlsx'):
                content = read_xlsx(filepath)
            else:
                continue

            try:
                file_results = {}
                for type, pattern in patterns.items():
                    matches = re.findall(pattern, content)
                    if matches:
                        file_results[type] = matches
                if file_results:
                    results.append((filepath, file_results))
            except Exception as e:
                logging.error(f"Failed to read {filepath}: {str(e)}")

    for result in results:
        filepath, data = result
        logging.info(f"Results for {filepath}:")
        for info_type, matches in data.items():
            logging.info(f"  Found {len(matches)} {info_type}(s): {matches}")

# Example usage
directory_to_scan = r'C:\Users\PC\Desktop\python\files'
scan_files(directory_to_scan)

