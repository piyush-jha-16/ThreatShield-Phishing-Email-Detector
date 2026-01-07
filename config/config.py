"""
Application configuration settings
"""
import os
import secrets
import tempfile

class Config:
    """Flask application configuration"""
    
    # Security
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(32))
    
    # File uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = tempfile.gettempdir()
    ALLOWED_EXTENSIONS = {'.eml'}
    
    # Database
    USERS_DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'users_db.json')
    
    # Session
    SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
