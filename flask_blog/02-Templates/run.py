from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Chi Thong',
        'title': 'Blog Post 1',
        'content': 'Noi dung dau tien',
        'date_posted': '8-9-2020'
    },
    {
        'author': 'Thanh Dung',
        'title': 'Blog Post 2',
        'content': 'Noi dung thu hai',
        'date_posted': '9-9-2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
    # posts data pass home.html


@app.route("/about")
def about():
    return render_template('about.html', title='About')
    # title la title browser


if __name__ == '__main__':
    app.run(debug=True)