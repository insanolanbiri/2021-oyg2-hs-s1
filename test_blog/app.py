from crypt import methods
import os

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


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegisterForm(request.form)
    if form.validate and request.method == "POST":
        username = form.username.data
        email = form.email.data
        password = username + form.password.data
        kayit = User(username=username, email=email, password=password)
        try:
            db.session.add(kayit)
            db.session.commit()
            return render_template("index.html", form=form, status="başarılı")
        except Exception as e:
            return render_template("index.html", form=form, status=f"bir şey oldu: {e}")
    else:
        return render_template("index.html", form=form, status="")
