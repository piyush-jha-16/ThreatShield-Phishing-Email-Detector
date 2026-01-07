"""
File handling utilities
"""
import os
from werkzeug.utils import secure_filename
from config.config import Config

def save_uploaded_file(file):
    """
    Save uploaded file to temp directory
    Returns: (success, filepath_or_error_message)
    """
    try:
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
        file.save(filepath)
        return True, filepath
    except Exception as e:
        return False, f'Error saving file: {str(e)}'

def cleanup_file(filepath):
    """Remove file from filesystem"""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
        return True
    except Exception as e:
        print(f"Error cleaning up file: {e}")
        return False
