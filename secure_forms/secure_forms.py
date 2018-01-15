from flask import Flask, render_template, flash, session, url_for, redirect, jsonify
from app_forms import MyForm, LoginForm
from user_model import User, Product
from peewee import OperationalError, IntegrityError
from flask_bcrypt import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "vjndbkgnkj.g,nm.dfjbdrgsD437i83u4h.dfjbdrgsD437i83u4h"

@app.route('/',methods=("GET","POST"))
def index():
    form = MyForm()
    if form.validate_on_submit():
        #everything is okay
        names = form.names.data
        email = form.email.data
        age = form.age.data
        password = form.password.data
        print("Names {0} Email {1} Age {2}".format(names, email, age))
        password = generate_password_hash(password)
        try:
            User.create(names=names, email=email, age=age, password=password)
            flash("The user was registered successfully ")
        except IntegrityError:
            flash("User by {0} email exists".format(email))

    return render_template("index.html", form=form)

@app.route('/login', methods=("GET", "POST"))
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user = User.get(User.email == email)
            check = check_password_hash(user.password, password)
            print(check)
            if check:
                print("Logged in successfully")
                # return render_template("products.html", user=user)
                session["names"] = user.names
                session["id"] = user.id
                return redirect(url_for("products"))
            else:
                flash("Wrong username or password")
        except Exception:
            flash("Wrong username or password")
    return render_template("login.html", form=form)

@app.route('/products')
def products():
    if "names" not in session:
        return redirect(url_for("login"))
    else:
        return  render_template("products.html", names=session["names"])

@app.route('/logout')
def logout():
    session.pop("names")
    session.pop("id")
    return redirect(url_for("login"))

if __name__ == '__main__':
    #User.drop_table()
    try:
        Product.create_table()
    except OperationalError:
        pass

    try:
        User.create_table()
    except OperationalError:
        pass
    app.run(port=8000)

    #host="0.0.0.0" port=8000
