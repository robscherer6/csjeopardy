from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/jeopardy')
def jeopardy():
    return render_template("jeopardy.html", user=current_user)

@views.route('/question/<int:category_id>/<int:point_value>/options')
def question_options(category_id, point_value):
    return render_template('question.html')

