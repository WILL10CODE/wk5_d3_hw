from flask import Blueprint, render_template, request
from flask_sqlalchemy import model
from .forms import LoginForm
from .models import User, db


user = Blueprint('user', __name__, template_folder='user_templates')
@user.route('/login', methods=["GET","POST"])
def logME():
    this_form = LoginForm()

    return render_template('user_index.html', form = this_form)

@user.route('/info', methods=["GET","POST"])
def seeME():
    my_model = User()
    if request.method == "POST":
        if my_model.validate():
            first_name = my_model.first_name.data
            last_name = my_model.last_name.data
            email = my_model.email.data
            password = my_model.password.data

            user= User(first_name, last_name, email, password)

            db.session.add

            

            

    return render_template( 'user_base.html', model = my_model)