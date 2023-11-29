from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "secret"
# debug = DebugToolbarExtension(app)
# DebugToolbarExtension would not install properly

@app.route("/")
def ask_questions():
    """Create form for MadLib inputs"""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)

@app.route("/madlib")
def show_madlib():
    """Displays generated madlib"""

    text = story.generate(request.args)

    return render_template("story.html",text=text)