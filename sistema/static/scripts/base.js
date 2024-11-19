 let tiempoInactividadPermitido = 50000
 let temporizador;

 function resetearTemporizador() {
    clearTimeout(temporizador);
    temporizador = setTimeout(cerrarSesionPorInactividad, tiempoInactividadPermitido);
 }

 function cerrarSesionPorInactividad() {

    document.getElementById('logoutForm').submit();
}


window.onload = resetearTemporizador;
document.onmousemove = resetearTemporizador;
document.onkeypress = resetearTemporizador;
document.onclick = resetearTemporizador;
document.onscroll = resetearTemporizador;

// modal cartel

document.addEventListener('DOMContentLoaded', function () {
   var modal = document.getElementById('modal');
   var closeBtn = document.querySelector('.close');

   // Verificar si el modal y el botón de cerrar existen
   if (modal && closeBtn) {
       // Mostrar modal si contiene mensajes
       if (modal.querySelector('p')) {
           modal.style.display = 'flex';
       }

       // Cerrar modal al hacer clic en la "x"
       closeBtn.addEventListener('click', function () {
           modal.style.display = 'none';
       });

       // Cerrar modal al hacer clic fuera del contenido
       window.addEventListener('click', function (event) {
           if (event.target === modal) {
               modal.style.display = 'none';
           }
       });
   }
});
