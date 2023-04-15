document.addEventListener('DOMContentLoaded', function () {
    const progressBar = document.getElementById('day-progress-bar');
    progressBar.addEventListener('click', toggleDayInverted);

    updateNavClock();
    updateDayProgressBar();
    updateDayPeriodicData();
  });


function updateDayPeriodicData () { 
  setInterval(updateNavClock, 1000);
  setInterval(updateDayProgressBar, 60000);
}

function updateNavClock() {
  var now = new Date();
  updateTimer("nav_clock", now );
}

let isDayBarInverted = false;

function toggleDayInverted() {
  isDayBarInverted = !isDayBarInverted;
  updateDayProgressBar();
}

function updateDayProgressBar() {
  const progressBar = document.getElementById('day-progress-bar');
  const progressText = document.getElementById('day_progress-text');
  progressPercentage = calculateDayProgressBarPercentage(isDayBarInverted);
  updateProgressBar(progressBar,progressText, progressPercentage, isDayBarInverted );
}

function calculateDayProgressBarPercentage(inverted){
  const currentTime = new Date();
  const startHour = 4;
  const endHour = 11;
  const totalMinutes = (endHour - startHour) * 60;
  const elapsedMinutes = currentTime.getHours()*60 + currentTime.getMinutes() - startHour * 60;
  progressPercentage = (elapsedMinutes / totalMinutes) * 100;
  if (inverted) {
    progressPercentage = 100 - progressPercentage;
  }
  return progressPercentage;
}







