import os
from functools import wraps

from flask import (
    Flask,
    Response,
    flash,
    logging,
    redirect,
    render_template,
    request,
    session,
    url_for,
    g,
)
from flask_sqlalchemy import SQLAlchemy
from wtforms import (
    DateField,
    Form,
    IntegerField,
    PasswordField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    TextAreaField,
    validators,
    widgets,
)

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////" + os.path.join(
    os.getcwd(), "test.db3"
)
app.config["SECRET_KEY"] = os.urandom(32)
db = SQLAlchemy(app)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for("login"))

    return decorated_function


class User(db.Model):
    __tablename__ = "user"
    username = db.Column(db.String(30), primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(255))


class RegisterForm(Form):
    username = StringField(
        "kullanıcı adı", validators=[validators.DataRequired("boş olmaz")]
    )
    email = StringField("e-posta", validators=[validators.Email("doğru gir")])
    password = PasswordField(
        "parola", validators=[validators.DataRequired("boş olmaz")]
    )
    confirm = PasswordField(
        "bi daha parola",
        validators=[
            validators.DataRequired("boş olmaz"),
            validators.EqualTo(password, "aynı gir"),
        ],
    )
    submit = SubmitField("kayıt")


class LoginForm(Form):
    username = StringField("kullanıcı adı")
    password = PasswordField("şifre")
    submit = SubmitField("giriş")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate and request.method == "POST":
        username = form.username.data
        email = form.email.data
        password = username + form.password.data
        kayit = User(username=username, email=email, password=password)
        try:
            db.session.add(kayit)
            db.session.commit()
            return render_template("register.html", form=form, status="başarılı")
        except Exception as e:
            return render_template(
                "register.html", form=form, status=f"bir şey oldu: {e}"
            )
    else:
        return render_template("register.html", form=form, status="")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate() and request.method == "POST":
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("auth"))
            else:
                pass
        else:
            pass
    return render_template("login.html", form=form)


@app.route("/auth")
@login_required
def auth():
    return render_template("auth.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
