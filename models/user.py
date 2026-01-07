"""
User database operations
"""
import json
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from config.config import Config

class UserDatabase:
    """Handle user data storage and retrieval"""
    
    def __init__(self):
        self.db_file = Config.USERS_DB_FILE
        self.users = self.load_users()
    
    def load_users(self):
        """Load users from JSON file"""
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading users: {e}")
                return {}
        return {}
    
    def save_users(self):
        """Save users to JSON file"""
        try:
            with open(self.db_file, 'w') as f:
                json.dump(self.users, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving users: {e}")
            return False
    
    def user_exists(self, username):
        """Check if username exists"""
        return username in self.users
    
    def create_user(self, username, email, password):
        """Create a new user"""
        if self.user_exists(username):
            return False, 'Username already exists'
        
        self.users[username] = {
            'email': email,
            'password': generate_password_hash(password),
            'created_at': datetime.now().isoformat()
        }
        
        if self.save_users():
            return True, 'User created successfully'
        return False, 'Error saving user data'
    
    def authenticate_user(self, username, password):
        """Authenticate user with username and password"""
        user = self.users.get(username)
        if not user:
            return False
        return check_password_hash(user['password'], password)
    
    def get_user(self, username):
        """Get user data by username"""
        return self.users.get(username)

# Global user database instance
user_db = UserDatabase()
