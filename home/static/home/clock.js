document.addEventListener('DOMContentLoaded', function () {
    console.log('page loaded');
    displayTime();
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
    setTimeout(displayTime, 1000);
}