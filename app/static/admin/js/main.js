function updateTime() {
    fetch('/time')
        .then(response => response.json())
        .then(data => {
            document.getElementById('clock').innerText = data.time;
        })
        .catch(error => console.error('Ошибка:', error));
}

setInterval(updateTime, 1000); // Обновлять каждую секунду
window.onload = updateTime;