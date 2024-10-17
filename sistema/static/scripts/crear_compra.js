document.addEventListener('DOMContentLoaded', function () {

    // Set current date in the Argentina timezone
    function setCurrentDate() {
        const argentinaTimezoneOffset = -3; // Argentina timezone offset (-3 hours from UTC)
        const today = new Date();
        today.setHours(today.getHours() + argentinaTimezoneOffset);
        const dateString = today.toISOString().split('T')[0];
        document.getElementById('fecha_hs').value = dateString;
    }
    setCurrentDate();

    // Variables to store total
    let totalCompra = 0;

    // Function to update the total value
    function actualizarTotal() {
        let total = 0;
        const filas = document.querySelectorAll('#tabla_compras tbody tr');
        filas.forEach(function(fila) {
            const subtotal = parseFloat(fila.querySelector('.subtotal').innerText);
            total += isNaN(subtotal) ? 0 : subtotal;
        });
        document.getElementById('total').value = total.toFixed(2);
    }

    // Add event listener to "Agregar Producto" buttons
    const botonesAgregar = document.querySelectorAll('.agregar-producto');
    botonesAgregar.forEach(function(boton) {
        boton.addEventListener('click', function() {
            const idProducto = this.getAttribute('data-id');
            const nombreProducto = this.getAttribute('data-nombre');
            const precioProducto = parseFloat(this.getAttribute('data-precio'));

            agregarProductoATabla(idProducto, nombreProducto, precioProducto);
        });
    });

    // Function to add product to the table
    function agregarProductoATabla(id, nombre, precio) {
        const tbody = document.querySelector('#tabla_compras tbody');

        // Create a new row
        const fila = document.createElement('tr');

        fila.innerHTML = `
            <td>${nombre}</td>
            <td>${precio.toFixed(2)}</td>
            <td><input type="number" value="1" min="1" class="cantidad" style="width: 60px;"></td>
            <td class="subtotal">${precio.toFixed(2)}</td>
            <td><button class="btn btn-danger eliminar-producto">Eliminar</button></td>
        `;

        // Add event listener to quantity change
        const cantidadInput = fila.querySelector('.cantidad');
        cantidadInput.addEventListener('change', function() {
            const cantidad = parseInt(this.value);
            const subtotal = precio * cantidad;
            fila.querySelector('.subtotal').innerText = subtotal.toFixed(2);
            actualizarTotal();
        });

        // Add event listener to "Eliminar" button
        const botonEliminar = fila.querySelector('.eliminar-producto');
        botonEliminar.addEventListener('click', function() {
            fila.remove();
            actualizarTotal();
        });

        // Append the row to the table body
        tbody.appendChild(fila);

        // Update the total
        actualizarTotal();
    }
});
