"""
Main routes (homepage, etc.)
"""
from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Render homepage"""
    return render_template('index.html')
