from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Información.html")

@app.route("/Apoya")
def Apoya():
    return render_template("Apoya.html")

@app.route("/Escritores")
def Escritores():
    return render_template("Sergio.html")

@app.route("/¡A_escribir!")
def A_escribir():
    return render_template("¡A_escribir!.html")

@app.route("/register")
def register():
    return render_template("/register.html")

@app.route("/login")
def login():
    return render_template("/login.html")
