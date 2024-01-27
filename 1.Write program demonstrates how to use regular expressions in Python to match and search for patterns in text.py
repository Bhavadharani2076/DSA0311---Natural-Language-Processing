#1
import re

def find_emails(text):
    # Define a simple regular expression for matching email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to find all matches in the text
    matches = re.findall(email_pattern, text)

    return matches

# Example text containing email addresses
sample_text = "Contact us at info@example.com or support@company.com for assistance."

# Find and print all email addresses in the text
email_addresses = find_emails(sample_text)
print("Email Addresses Found:")
print(email_addresses)
