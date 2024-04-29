import os
import re
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scan_files(directory):
    results = []
    # Expanded dictionary with additional patterns for sensitive information
    patterns = {
        'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        'social_security_number': r'\b\d{3}-\d{2}-\d{4}\b',
        'credit_card_number': r'\b(?:\d{4}[- ]?){3}\d{4}\b',
        'phone_number': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        'date_of_birth': r'\b(?:0[1-9]|1[0-2])[-/.](?:0[1-9]|[12][0-9]|3[01])[-/.](?:19|20)\d{2}\b'
    }
    
    # Traverse the directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                permissions = os.stat(filepath).st_mode
                if (permissions & 0o777) > 0o644:
                    logging.warning(f"Permissions for {filepath} are too permissive ({oct(permissions)[-3:]}).")
                
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    file_results = {}
                    for type, pattern in patterns.items():
                        matches = re.findall(pattern, content)
                        if matches:
                            file_results[type] = matches
                    if file_results:
                        results.append((filepath, file_results))
            except Exception as e:
                logging.error(f"Failed to read {filepath}: {str(e)}")

    # Print summary of findings
    for result in results:
        filepath, data = result
        logging.info(f"Results for {filepath}:")
        for info_type, matches in data.items():
            logging.info(f"  Found {len(matches)} {info_type}(s): {matches}")

# Example usage
directory_to_scan = '/path/to/your/directory'
scan_files(directory_to_scan)
