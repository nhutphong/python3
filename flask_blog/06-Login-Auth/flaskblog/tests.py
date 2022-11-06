from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/test-form", methods=['GET', 'POST'])
def test_form():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))

    form = LoginForm()
    context = {}
    context['stringfield'] = vars(form.email)
    context['passwordfield'] = vars(form.password)
    context['booleanfield'] = vars(form.remember)
    context['submitfield'] = vars(form.submit)

    return render_template('tests.html', title='tests', form=form, **context)


@app.route("/test-render")
def test_render():

    html = f"""
        <article class="media content-section">
          <div class="media-body">
              <h1> { current_user }</h1>
          </div>
        </article>
    """

    return html