from flask import Flask, render_template
from utils.excel_manager import cargar_y_normalizar

app = Flask(__name__)

@app.route("/")
def home():

    registros = cargar_y_normalizar("software")

    return render_template(
        "index.html",
        registros=registros
    )

if __name__ == "__main__":
    app.run(debug=True)