"""
Email analysis routes
"""
from flask import Blueprint, request, jsonify
from detection.detector import PhishingDetector
from utils.validators import validate_file_upload
from utils.file_handler import save_uploaded_file, cleanup_file
from utils.email_parser import parse_eml_file

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/api/analyze-manual', methods=['POST'])
def analyze_manual():
    """Analyze manually entered email data"""
    data = request.json
    email_data = {
        'sender': data.get('sender', ''),
        'subject': data.get('subject', ''),
        'body': data.get('body', ''),
        'headers': {},
        'attachments': []
    }
    
    # Analyze email
    detector = PhishingDetector()
    result = detector.analyze_email(email_data)
    
    return jsonify({
        'success': True,
        'result': result
    })

@analysis_bp.route('/api/analyze-file', methods=['POST'])
def analyze_file():
    """Analyze uploaded .eml file"""
    if 'file' not in request.files:
        return jsonify({'success': False, 'message': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'message': 'No file selected'}), 400
    
    # Validate file
    is_valid, error_msg = validate_file_upload(file.filename)
    if not is_valid:
        return jsonify({'success': False, 'message': error_msg}), 400
    
    # Save uploaded file
    success, result = save_uploaded_file(file)
    if not success:
        return jsonify({'success': False, 'message': result}), 500
    
    filepath = result
    
    try:
        # Parse email file
        email_data = parse_eml_file(filepath)
        
        # Analyze email
        detector = PhishingDetector()
        analysis_result = detector.analyze_email(email_data)
        
        # Clean up file
        cleanup_file(filepath)
        
        return jsonify({
            'success': True,
            'result': analysis_result,
            'email_preview': {
                'sender': email_data['sender'],
                'subject': email_data['subject'],
                'body_preview': email_data['body'][:200] + '...' if len(email_data['body']) > 200 else email_data['body']
            }
        })
    
    except Exception as e:
        cleanup_file(filepath)
        return jsonify({'success': False, 'message': f'Error parsing file: {str(e)}'}), 500
