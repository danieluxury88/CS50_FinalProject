document.addEventListener('DOMContentLoaded', function () {
    displayTime();
    updateTimer();
});

function displayTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();
    minutes = minutes < 10 ? '0'+minutes : minutes;
    seconds = seconds < 10 ? '0'+seconds : seconds;
    var time = hours + ':' + minutes + ':' + seconds;
    document.getElementById('clock').innerHTML = time;
    setTimeout(displayTime, 400);
}

function updateTimer() {
    var end_time = new Date(end_time_str);
    var remaining = Math.floor((end_time - new Date()) / 1000);
    var hours = Math.floor(remaining / 3600);
    var minutes = Math.floor((remaining % 3600) / 60).toString().padStart(2, '0');
    var seconds = (remaining % 60).toString().padStart(2, '0');
    var display = hours + ":" + minutes + ":" + seconds;
    document.getElementById("time-remaining").textContent = display;
    setTimeout(updateTimer, 400);
}

