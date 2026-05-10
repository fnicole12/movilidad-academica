from flask import Flask, render_template, request
from utils.excel_manager import cargar_y_normalizar
from utils.excel_manager import (
    cargar_y_normalizar,
    guardar_historial,
    obtener_carreras
)

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
        nombre = request.form.get("nombre")
        registro = request.form.get("registro")
        
        busqueda_realizada = True

    registros = cargar_y_normalizar(carrera)

    # Obtener semestres únicos
    semestres = []
    for r in registros:
        semestre = r["semestre"]
        if semestre not in semestres:
            semestres.append(semestre)

    # Obtener universidades según semestre
    registros_para_universidades = registros
    if semestre_seleccionado != "":
        registros_para_universidades = [
            r for r in registros
            if r["semestre"] == semestre_seleccionado
        ]
    universidades = []
    for r in registros_para_universidades:
        universidad = r["universidad"]
        if universidad not in universidades:
            universidades.append(universidad)
    
    # Resetear universidad inválida
    if universidad_seleccionada not in universidades:
        universidad_seleccionada = ""

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

    if busqueda_realizada:
        guardar_historial({
            "nombre": nombre,
            "registro": registro,
            "carrera": carrera,
            "semestre": semestre_seleccionado,
            "universidad": universidad_seleccionada
        })
    
    carreras = obtener_carreras()

    return render_template(
        "index.html",
        carreras=carreras,
        carrera=carrera,
        registros=registros,
        semestres=semestres,
        universidades=universidades,
        semestre_seleccionado=semestre_seleccionado,
        universidad_seleccionada=universidad_seleccionada,
        busqueda_realizada=busqueda_realizada
    )







if __name__ == "__main__":
    app.run(debug=True)