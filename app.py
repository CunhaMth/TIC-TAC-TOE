from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "velha123"

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/jogo", methods=["POST"])
def jogo():
    simbolo = request.form.get("simbolo")
    session["simbolo"] = simbolo
    return render_template("jogo.html", simbolo=simbolo)

if __name__ == "__main__":
    app.run(debug=True)