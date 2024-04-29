# File Security Analyzer

This simple Python script securely scans files within a specified directory to identify and report potentially sensitive information, including email addresses, IP addresses, social security numbers, credit card details, phone numbers, and dates of birth. Designed to run locally on your machine, it ensures that all results remain private and are not exposed to external risks. Additionally, the script assesses file permissions, alerting users if settings are more permissive than recommended, thereby enhancing data security.

The script is intended for use in environments where data security and privacy are paramount, and it complies with best practices for handling and processing sensitive information securely.

## Features

### Sensitive Data Detection
- **Comprehensive Scanning:** The script efficiently scans files within a specified directory for various types of sensitive information, including email addresses, IP addresses, social security numbers, credit card details, phone numbers, and dates of birth. This ensures thorough identification of potential data leakage points in stored files.

### Permission Check
- **Security-Oriented File Permission Analysis:** Before processing each file, the script evaluates the file permissions using `os.stat()`. It logs a warning if the file permissions are more permissive than `644`, highlighting files that are potentially insecure because they are writable by users other than the owner or readable by all users. This feature is crucial for maintaining data security and integrity, ensuring that sensitive files are adequately protected against unauthorized access.

### Logging
- **Detailed and Secure Logging:** All findings and notable events during the scanning process are meticulously logged. The logging is designed to avoid direct exposure of sensitive data:
  - **Secure Log Files:** Logs are written to a dedicated file (`file_scan_log.log`), which helps in tracking the activities of the script without displaying sensitive information on standard output.
  - **Error Handling Logs:** Enhanced error handling within the script ensures that operational issues, especially those related to file access, are logged. This helps in diagnosing problems during the scanning process and ensures robust behavior under various file system conditions.
  - **Privacy-Focused Data Handling:** The logs detail the types and counts of sensitive information found without revealing the actual data, aligning with best practices for data privacy and security.

These features make the script an effective tool for environments where data security and privacy are paramount, ensuring that sensitive information is handled with the highest standards of care.

### Sequence
![Sequence Diagram](https://i.ibb.co/yPmfM5R/sequence.png)

**Breakdown of the interactions:**
1. User to System: The user initiates the scanning process by sending a request to the system.
2. System to File System: The system, upon receiving the user's request, communicates with the file system to request access to the files that need to be scanned.
3. File System to Logger: As the file system processes the request, it logs details of the file access to a logging system or logger. This ensures that all file access activities are recorded for security or auditing purposes.
4. System Processing Files: The system processes the files according to the scanning criteria set by the user or the application logic. This involves reading, analyzing, and perhaps extracting information from the files.
5. System to User: After processing the files, the system sends the results back to the user. This might include a report on what was found in the files or any actions taken based on the file content.
6. Logger Activity: The logger continuously logs all activities, including file access and processing actions, providing a traceable record of operations for review or troubleshooting.

### Result
![File security Analyzer Log](https://i.ibb.co/xzKXX7n/filesecurity.png)

## Security and Compliance Considerations:

- **Data Privacy:** Users are responsible for ensuring that all data processing complies with applicable data protection laws, such as the General Data Protection Regulation (GDPR) or the Health Insurance Portability and Accountability Act (HIPAA). Users should implement appropriate measures to secure data and potentially seek consent where required by law.

- **Best Practices:** It is recommended to adopt data minimization principles, only processing the minimal amount of sensitive data necessary and considering data anonymization techniques where feasible.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.x

### Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/cybrsen/filesecurityanalyzer.git


## Contribution
Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Licence
This project is licensed under the MIT License - see the LICENSE.md file for details.


## Legal disclaimer

This script is provided as-is without any express or implied warranties. While every effort has been made to ensure the functionality and security of the script, the users of this script are solely responsible for ensuring compliance with applicable data protection laws.

Users must ensure that they have the legal authority to process the data analyzed by this script, and must implement suitable data protection and security measures. This script is intended to aid users in identifying potential sensitive data, and should not be solely relied upon for achieving compliance with data protection laws. Users should consult with a legal advisor to understand their obligations under applicable laws.

It is also the user's responsibility to obtain necessary consent and provide any required notices to data subjects whose data might be processed by this script. Ensure that any data handled by this script is done so in a lawful, fair, and transparent manner.

