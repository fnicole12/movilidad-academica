function reiniciarFiltros() {
    document.querySelector(
        'select[name="semestre"]'
    ).value = ""
    document.querySelector(
        'select[name="universidad"]'
    ).value = ""
    document.getElementById(
        "filtro-form"
    ).submit()
}