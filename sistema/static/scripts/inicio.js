




    document.addEventListener('DOMContentLoaded', function () {
        var ctx = document.getElementById('stockChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Producto 1', 'Producto 2', 'Producto 3'],
                datasets: [{
                    data: [10, 20, 30],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)'
                    ],
                    borderWidth: 1
                }]
            }
        });
    });

