"""
Input validation utilities
"""
import re

def validate_registration_input(username, email, password):
    """
    Validate registration form input
    Returns: (is_valid, error_message)
    """
    # Check if all fields are provided
    if not username or not email or not password:
        return False, 'All fields are required'
    
    # Validate username
    username = username.strip()
    if len(username) < 3:
        return False, 'Username must be at least 3 characters'
    if len(username) > 30:
        return False, 'Username must be less than 30 characters'
    if not re.match(r'^[a-zA-Z0-9_-]+$', username):
        return False, 'Username can only contain letters, numbers, underscores, and hyphens'
    
    # Validate email
    email = email.strip()
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        return False, 'Invalid email address'
    
    # Validate password
    if len(password) < 8:
        return False, 'Password must be at least 8 characters'
    if len(password) > 128:
        return False, 'Password is too long'
    
    return True, None

def validate_login_input(username, password):
    """
    Validate login form input
    Returns: (is_valid, error_message)
    """
    if not username or not password:
        return False, 'All fields are required'
    
    username = username.strip()
    if not username:
        return False, 'Username is required'
    
    if not password:
        return False, 'Password is required'
    
    return True, None

def validate_file_upload(filename):
    """
    Validate uploaded file
    Returns: (is_valid, error_message)
    """
    if not filename:
        return False, 'No file selected'
    
    if not filename.endswith('.eml'):
        return False, 'Only .eml files are supported'
    
    return True, None

def sanitize_input(text):
    """Remove potentially harmful characters from input"""
    if not text:
        return ''
    return text.strip()
