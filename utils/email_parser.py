"""
Email parsing utilities
"""
from email import policy
from email.parser import BytesParser

def parse_eml_file(file_path):
    """
    Parse .eml file and extract relevant information
    Returns: dict with sender, subject, body, headers, attachments
    """
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)
    
    # Extract headers
    headers = {}
    for key in msg.keys():
        headers[key] = msg.get(key)
    
    # Extract sender
    sender = msg.get('From', '')
    subject = msg.get('Subject', '')
    
    # Extract body
    body = ''
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                body += part.get_payload(decode=True).decode('utf-8', errors='ignore')
    else:
        body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
    
    # Extract attachments
    attachments = []
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                attachments.append(part.get_filename() or 'unknown')
    
    return {
        'sender': sender,
        'subject': subject,
        'body': body,
        'headers': headers,
        'attachments': attachments
    }
