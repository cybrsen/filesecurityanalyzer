# File Security Analyzer

This Python script securely scans files within a specified directory to identify and report potentially sensitive information, including email addresses, IP addresses, social security numbers, credit card details, phone numbers, and dates of birth. Designed to run locally on your machine, it ensures that all results remain private and are not exposed to external risks. Additionally, the script assesses file permissions, alerting users if settings are more permissive than recommended, thereby enhancing data security.

The script is intended for use in environments where data security and privacy are paramount, and it complies with best practices for handling and processing sensitive information securely.

## Features

- **Sensitive Data Detection**: Scan for various types of sensitive data.
- **Permission Check**: Evaluate file permissions and highlight potential security risks.
- **Logging**: Detailed logs of all findings and errors during the scanning process.

## Security and Compliance Considerations:

- Data Privacy: Users are responsible for ensuring that all data processing complies with applicable data protection laws, such as the General Data Protection Regulation (GDPR) or the Health Insurance Portability and Accountability Act (HIPAA). Users should implement appropriate measures to secure data and potentially seek consent where required by law.

- Best Practices: It is recommended to adopt data minimization principles, only processing the minimal amount of sensitive data necessary and considering data anonymization techniques where feasible.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What you need to install the software:

- Python 3.x

### Installing

1. Clone the repository:
   ```bash
   git clone https://github.com/cybrsen/filesecurityanalyzer.git

### Result
![File Security Analyzer](https://i.ibb.co/C85FpSQ/filesecurityanalyzer.png)

### Legal disclaimer

This script is provided as-is without any express or implied warranties. While every effort has been made to ensure the functionality and security of the script, the users of this script are solely responsible for ensuring compliance with applicable data protection laws.

Users must ensure that they have the legal authority to process the data analyzed by this script, and must implement suitable data protection and security measures. This script is intended to aid users in identifying potential sensitive data, and should not be solely relied upon for achieving compliance with data protection laws. Users should consult with a legal advisor to understand their obligations under applicable laws.

It is also the user's responsibility to obtain necessary consent and provide any required notices to data subjects whose data might be processed by this script. Ensure that any data handled by this script is done so in a lawful, fair, and transparent manner.

