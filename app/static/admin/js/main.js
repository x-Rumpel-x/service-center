// JavaScript
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

// Первый запуск сразу при загрузке страницы
document.addEventListener('DOMContentLoaded', updateTime);

// Обновление каждую секунду
const timer = setInterval(updateTime, 1000);

// Опционально: остановка таймера при необходимости
// clearInterval(timer);