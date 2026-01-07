"""
Authentication routes
"""
from flask import Blueprint, request, jsonify, session
from models.user import user_db
from utils.validators import validate_registration_input, validate_login_input

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    """Handle user registration"""
    data = request.json
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '')
    
    # Validate input
    is_valid, error_msg = validate_registration_input(username, email, password)
    if not is_valid:
        return jsonify({'success': False, 'message': error_msg}), 400
    
    # Create user
    success, message = user_db.create_user(username, email, password)
    
    if success:
        return jsonify({'success': True, 'message': 'Registration successful'})
    else:
        return jsonify({'success': False, 'message': message}), 400

@auth_bp.route('/api/login', methods=['POST'])
def login():
    """Handle user login"""
    data = request.json
    username = data.get('username', '').strip()
    password = data.get('password', '')
    
    # Validate input
    is_valid, error_msg = validate_login_input(username, password)
    if not is_valid:
        return jsonify({'success': False, 'message': error_msg}), 400
    
    # Authenticate user
    if user_db.authenticate_user(username, password):
        session['username'] = username
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

@auth_bp.route('/api/logout', methods=['POST'])
def logout():
    """Handle user logout"""
    session.pop('username', None)
    return jsonify({'success': True})
