from flask import Blueprint
from flask import render_template

user = Blueprint('user', __name__, template_folder='user_templates')
@user.route('/login')
def logME():
    return render_template('user_index.html')