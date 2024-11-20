document.addEventListener('DOMContentLoaded', function () {
    const buscarProducto = document.getElementById('buscarProducto');
    const listaProductos = document.getElementById('lista_productos');

    buscarProducto.addEventListener('input', function () {
        const filtro = buscarProducto.value.toLowerCase().trim(); // Convertir a minúsculas y eliminar espacios extra
        const filas = listaProductos.querySelectorAll('tr');

        let hayCoincidencias = false; // Indica si hay coincidencias

        filas.forEach(fila => {
            const celdas = fila.querySelectorAll('td');
            let coincidencia = false;

            // Verificar cada celda de la fila para encontrar coincidencias
            celdas.forEach(celda => {
                if (celda.textContent.toLowerCase().includes(filtro)) {
                    coincidencia = true;
                }
            });

            // Mostrar u ocultar la fila según la coincidencia
            if (coincidencia) {
                fila.style.display = '';
                hayCoincidencias = true;
            } else {
                fila.style.display = 'none';
            }
        });

        // Mostrar mensaje si no hay coincidencias
        const filaNoProductos = document.querySelector('.no_productos');
        if (!hayCoincidencias) {
            if (filaNoProductos) filaNoProductos.style.display = ''; // Mostrar fila "No hay artículos"
        } else {
            if (filaNoProductos) filaNoProductos.style.display = 'none'; // Ocultar fila "No hay artículos"
        }
    });
});


//MENSAJE DE ERROR
document.addEventListener('DOMContentLoaded', function () {
    var modal = document.getElementById('modal');
    var closeBtn = document.querySelector('.close');

    if (modal && closeBtn) {
        if (modal.querySelector('p')) {
            modal.style.display = 'flex';
        }

        closeBtn.addEventListener('click', function () {
            modal.style.display = 'none';
        });

        window.addEventListener('click', function (event) {
            if (event.target === modal) {
                modal.style.display = 'none';
            }
        });
    }
});