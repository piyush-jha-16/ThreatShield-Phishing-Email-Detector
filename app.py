"""
ThreatShield - Email Phishing Detection System
Main Flask application entry point
"""
from flask import Flask
from config.config import Config

def create_app():
    """Create and configure Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Register blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.analysis import analysis_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(analysis_bp)
    
    return app

# Create app instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)

