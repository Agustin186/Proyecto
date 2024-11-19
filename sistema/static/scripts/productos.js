
//BARRA DE BUSQUEDA
document.addEventListener('DOMContentLoaded', function () {
    const buscarProductoInput = document.getElementById('buscarProducto');
    const listaProductos = document.getElementById('lista-productos');

    if (buscarProductoInput && listaProductos) {
        buscarProductoInput.addEventListener('input', function () {
            const filtro = buscarProductoInput.value.toLowerCase();

            listaProductos.querySelectorAll('tr').forEach(tr => {
                const nombreProducto = tr.cells[1]?.textContent.toLowerCase() || ''; // Columna del nombre
                const codigoProducto = tr.cells[0]?.textContent.toLowerCase() || ''; // Columna del código

                if (nombreProducto.includes(filtro) || codigoProducto.includes(filtro)) {
                    tr.style.display = ''; // Mostrar fila si coincide
                } else {
                    tr.style.display = 'none'; // Ocultar fila si no coincide
                }
            });
        });
    } else {
        console.error('No se encontraron los elementos necesarios para la búsqueda.');
    }
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