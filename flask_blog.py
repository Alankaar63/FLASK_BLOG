from doctest import debug

from flask import Flask,render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__) #flask run --host=0.0.0.0
app.config['SECRET_KEY'] = '617d0df546173214dbc61cc5a8ab7527843a'
posts = [
    {
        'title' : 'Blog Post 1',
        'author': 'Donquixote Doflamingo',
        'content' : 'Regarding Dressrosa',
        'date_posted' : '28th Sept, 2025'
    },
    {
        'title' : 'Blog Post 2',
        'author': 'Trafalgar Law',
        'content' : 'Regarding Corazon',
        'date_posted' : '29th Sept, 2025'
    }
]

about_content = [
    {
        'person':"My name is Yoshikage Kira. I'm"
        "33 years old. My house is in the northeast block."
    },
    {
        'stand': 'bites the dust!'
    }
]
@app.route("/")
@app.route("/home")
def func():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',about_content=about_content)

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)

if __name__ == "__main__":
    app.run(debug=True)