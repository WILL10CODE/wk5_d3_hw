from urllib import response
from flask import Blueprint,render_template, redirect, url_for,request
# from flask_login import current_user, login_required

from .forms import CreatePostForm
blog = Blueprint('blog', __name__, template_folder='blog_templates')
# from app.models import Post


@blog.route('/blog_post')
def blog_2():
    return render_template('blog.html')

@blog.route('/profile')
def my_profile():
    response = {
        "name": "William",
        "about": "Hello! My name is William. How are you?" 
    }

    return response
