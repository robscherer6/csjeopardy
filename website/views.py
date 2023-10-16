from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

# @views.route('/')
# def home():
#     return render_template("jeopardy.html")

@views.route('/question/<int:category_id>/<int:point_value>/options')
def question_options(category_id, point_value):
    return render_template('question.html')

