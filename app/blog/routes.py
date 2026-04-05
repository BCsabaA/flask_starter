from flask import render_template
from . import blog_bp

@blog_bp.route('/')
def index():
    return 'Blog index page'