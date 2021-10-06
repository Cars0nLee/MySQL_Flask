from flask import Flask, render_template, redirect, request
from names import Name

app = Flask(__name__)

@app.route("/")
def index():
    names = Name.get_names()
    print(names)
    return render_template("read.html", nameshtml = names)


@app.route("/user", methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Name.create(data)
    return redirect("/")

@app.route("/add")
def add():
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)