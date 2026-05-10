# movilidad-academica

Sistema web local para consulta de equivalencias académicas entre programas de intercambio universitario.

El sistema permite:

- Consultar materias equivalentes entre UAG y universidades extranjeras.
- Filtrar por carrera.
- Filtrar por semestre.
- Filtrar por universidad.
- Registrar historial de consultas realizadas.
- Escalar fácilmente agregando nuevas sheets de Excel.

---

# Tecnologías utilizadas

- Python 3
- Flask
- Pandas
- HTML5
- CSS3
- JavaScript

---

# Estructura del proyecto

```text
movilidad-academica-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── materias.xlsx
│   └── historial_consultas.xlsx
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
└── utils/
    └── excel_manager.py
```

---

# Instalación

## 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd movilidad-academica-app
```

---

## 2. Crear entorno virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración de Excel

Colocar el archivo:

```text
materias.xlsx
```

dentro de:

```text
data/
```

Cada carrera debe estar representada por una sheet distinta dentro del mismo archivo Excel.

Ejemplo:

```text
MAPEO IDS
MAPEO ITA
MAPEO IA
```

La configuración de sheets se realiza en:

```text
utils/excel_manager.py
```

---

# Ejecutar aplicación

```bash
python app.py
```

El sistema estará disponible en:

```text
http://127.0.0.1:5000
```

---

# Funcionalidades

## Consulta de equivalencias

El usuario puede:

- Seleccionar carrera.
- Filtrar por semestre.
- Filtrar por universidad.
- Visualizar materias equivalentes.

---

## Historial de consultas

Cada búsqueda realizada se almacena automáticamente en:

```text
data/historial_consultas.xlsx
```

---

## Escalabilidad

Para agregar una nueva carrera:

1. Agregar nueva sheet en `materias.xlsx`
2. Registrar la configuración en:

```python
SHEETS_CARRERA = {
    ...
}
```

No es necesario modificar el frontend.

---

# Notas

- No abrir `historial_consultas.xlsx` mientras el sistema esté ejecutándose.
- El sistema está diseñado para ejecutarse localmente.
- Compatible con Windows, Linux y macOS.

---

# Autores
Fernanda Nicole García Melendrez
Directora Natalia Madrid Zapata

Proyecto desarrollado para apoyo a procesos de movilidad académica universitaria.