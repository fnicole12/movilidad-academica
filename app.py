from flask import Flask, render_template, request
from utils.excel_manager import cargar_y_normalizar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    carrera = "software"
    semestre_seleccionado = ""
    universidad_seleccionada = ""
    busqueda_realizada = False

    if request.method == "POST":
        carrera = request.form.get("carrera")
        semestre_seleccionado = request.form.get("semestre")
        universidad_seleccionada = request.form.get("universidad")
        
        busqueda_realizada = True

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

    # Filtro semestre
    if semestre_seleccionado != "":
        registros = [
            r for r in registros
            if r["semestre"] == semestre_seleccionado
        ]

    # Filtro universidad
    if universidad_seleccionada != "":
        registros = [
            r for r in registros
            if r["universidad"] == universidad_seleccionada
        ]

    
    if not busqueda_realizada:
        registros = []

    return render_template(
        "index.html",
        registros=registros,
        semestres=semestres,
        universidades=universidades,
        semestre_seleccionado=semestre_seleccionado,
        universidad_seleccionada=universidad_seleccionada,
        busqueda_realizada=busqueda_realizada
    )







if __name__ == "__main__":
    app.run(debug=True)