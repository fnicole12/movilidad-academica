from flask import Flask, render_template, request
from utils.excel_manager import cargar_y_normalizar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    carrera = "software"
    semestre_seleccionado = ""

    if request.method == "POST":

        carrera = request.form.get("carrera")

        semestre_seleccionado = request.form.get("semestre")

    registros = cargar_y_normalizar(carrera)

    # Obtener semestres únicos
    semestres = []

    for r in registros:

        semestre = r["semestre"]

        if semestre not in semestres:

            semestres.append(semestre)

    # Obtener universidades únicas
    universidades = []

    for r in registros:

        universidad = r["universidad"]

        if universidad not in universidades:

            universidades.append(universidad)

    # Filtrar por semestre
    if semestre_seleccionado != "":

        registros = [

            r for r in registros

            if r["semestre"] == semestre_seleccionado
        ]

    return render_template(
        "index.html",
        registros=registros,
        semestres=semestres,
        universidades=universidades,
        semestre_seleccionado=semestre_seleccionado
    )

if __name__ == "__main__":
    app.run(debug=True)