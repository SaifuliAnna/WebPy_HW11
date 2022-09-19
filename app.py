from flask import Flask, render_template, request, redirect
from models import Contact, db_session

app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/", strict_slashes=False)
def index():
    contacts = db_session.query(Contact).all()
    return render_template("index.html", contacts=contacts)


@app.route("/detail/<id>", strict_slashes=False)
def detail(id):
    contact = db_session.query(Contact).filter(Contact.id == id).first()
    return render_template("detail.html", contact=contact)


@app.route("/contact/", methods=["GET", "POST"], strict_slashes=False)
def add_contact():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        name = request.form.get("name")
        surname = request.form.get("surname")
        phone = request.form.get("phone")
        email = request.form.get("email")
        birthday = request.form.get("birthday")
        address = request.form.get("address")
        contact = Contact(nickname=nickname, name=name, surname=surname,
                          phone=phone, email=email, birthday=birthday, address=address)
        db_session.add(contact)
        db_session.commit()
        return redirect("/")

    return render_template("contact.html")


@app.route("/delete/<id>", strict_slashes=False)
def delete(id):
    db_session.query(Contact).filter(Contact.id == id).delete()
    db_session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run()
