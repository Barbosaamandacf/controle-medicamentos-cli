from flask import Flask, render_template
from database import listar_medicamentos

app = Flask(__name__)


@app.route("/")
def home():
    medicamentos = listar_medicamentos()

    return render_template("index.html", medicamentos=medicamentos)


if __name__ == "__main__":
    app.run(debug=True)
