from flask import Flask, render_template, request, redirect
from models import Contact, Info, db_session

app = Flask(__name__)
app.debug = True
app.env = "development"


@app.route("/", strict_slashes=False)
def index():
    contacts = db_session.query(Contact).all()
    infos = db_session.query(Info).all()
    return render_template("index.html", contacts=contacts, infos=infos)


@app.route("/detail/<id>", strict_slashes=False)
def detail(id):
    contact = db_session.query(Contact).filter(Contact.id == id).first()
    info = db_session.query(Info).filter(Info.id == id).first()
    return render_template("detail.html", contact=contact, info=info)


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
        contact = Contact(nickname=nickname, phone=phone)
        db_session.add(contact)
        db_session.commit()
        info = Info(name=name, surname=surname, email=email,
                    birthday=birthday, address=address, info_id=contact.id)
        db_session.add(info)
        db_session.commit()
        return redirect("/")

    return render_template("contact.html")


@app.route("/delete/<id>", strict_slashes=False)
def delete(id):
    db_session.query(Contact).filter(Contact.id == id).delete()
    db_session.query(Info).filter(Info.id == id).delete()
    db_session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run()
