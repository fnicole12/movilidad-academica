import pandas as pd

ARCHIVOS_CARRERA = {
    "software": {
        "archivo": "data/materias.xlsx",
        "sheet": "MAPEO IDS"
    }
}

def cargar_y_normalizar(carrera):

    info = ARCHIVOS_CARRERA.get(carrera)

    if not info:
        return []

    try:

        df = pd.read_excel(
            info["archivo"],
            sheet_name=info["sheet"]
        )

        registros = []

        semestre_actual = None

        columnas = df.columns.tolist()

        # Primera columna = materias UAG
        columna_materia = columnas[0]

        # Universidades empiezan después
        universidades = columnas[3:]

        # Limpiar columnas basura
        universidades_limpias = []

        for u in universidades:

            if "Unnamed" in str(u):
                continue

            universidades_limpias.append(u)

        universidades = universidades_limpias

        # Recorrer filas
        for _, fila in df.iterrows():

            materia = fila[columna_materia]

            if pd.isna(materia):
                continue

            materia = str(materia).strip()

            # Detectar semestre
            if "SEMESTRE" in materia.upper():

                semestre_actual = materia

                continue

            # Ignorar filas basura
            if materia.upper() in [
                "INTERCAMBIO",
                "OPTATIVAS FORMACIÓN PROFESIONAL",
                "OPTATIVAS FORMACIÓN UNIVERSITARIA"
            ]:
                continue

            # Revisar equivalencias
            for universidad in universidades:

                equivalencia = fila[universidad]

                if pd.isna(equivalencia):
                    continue

                universidad = str(universidad)\
                    .replace("_x000D_", "")\
                    .strip()

                equivalencia = str(equivalencia)\
                    .replace("_x000D_", "")\
                    .strip()

                if equivalencia == "":
                    continue

                if equivalencia == "?":
                    continue

                if "http" in equivalencia.lower():
                    continue

                if equivalencia.lower() == "curriculum":
                    continue

                registros.append({
                    "semestre": semestre_actual,
                    "materia_uag": materia,
                    "universidad": universidad,
                    "materia_equivalente": equivalencia
                })

        return registros

    except Exception as e:

        print(f"Error procesando Excel: {e}")

        return []