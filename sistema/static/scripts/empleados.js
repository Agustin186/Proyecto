document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById("mensaje-modal");
    var span = document.getElementsByClassName("close restringuido")[0];

    // Mostrar el modal si existe
    if (modal) {
        modal.style.display = "flex";
    }

    // Cuando el usuario hace clic en la "x", se cierra el modal
    span.onclick = function() {
        modal.style.display = "none";
    };

    // Cuando el usuario hace clic fuera del contenido del modal, también se cierra
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});