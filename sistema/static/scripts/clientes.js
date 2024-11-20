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