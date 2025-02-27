function updateTime() {
    fetch('/time')
        .then(response => response.json())
        .then(data => {
            document.getElementById('clock').innerText = data.time;
            document.getElementById('date').innerText = data.date;
            document.getElementById('weekday').innerText = data.weekday;
        })
        .catch(error => console.error('Ошибка:', error));
}

document.addEventListener('DOMContentLoaded', updateTime);

const timer = setInterval(updateTime, 1000);
// Опционально: остановка таймера при необходимости
// clearInterval(timer);

$(document).ready(function() {
    $('#hide-menu').on('click', function(e) {
        e.preventDefault(); // Отменяем стандартное действие ссылки
        console.log("1")
    });
});