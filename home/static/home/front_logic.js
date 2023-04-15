document.addEventListener('DOMContentLoaded', function () {
    const progressBar = document.getElementById('day-progress-bar');
    progressBar.addEventListener('click', toggleInverted);
    
    const cycle_progressBar = document.getElementById('cycle-progress-bar');
    cycle_progressBar.addEventListener('click', toggleCycleBar);

    const nav_cycle_time_lbl = document.getElementById('nav_cycle_lbl_time');
    nav_cycle_time_lbl.addEventListener('click', toggleCycleBar);

    updateNavClock();
    updateNavCycleTimer();
    updateDayProgressBar();
    updateCycleProgressBar();
    updatePeriodicData();

  });

function updatePeriodicData () { 
  setInterval(updateNavClock, 1000);
  setInterval(updateDayProgressBar, 60000);
  setInterval(updateCycleProgressBar, 60000); // Update every minute
  setInterval(updateNavCycleTimer, 500); // Update every minute
}

function updateTimer(element_id, timer) {
  const hours = timer.getHours();
  const minutes = timer.getMinutes();
  const seconds = timer.getSeconds();
  const timeString = `${hours}:${padZero(minutes)}:${padZero(seconds)}`;
  UpdateStringTimer(element_id,timeString );
}

function padZero(number) {
  return number < 10 ? "0" + number : number;
}

function UpdateStringTimer(element_id, timeString ) {
  document.getElementById(element_id).innerHTML = timeString;
}

function updateNavClock() {
  var now = new Date();
  updateTimer("nav_clock", now );
}

let isDayBarInverted = false;

function toggleInverted() {
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
  const startHour = 6;  // 6 AM
  const endHour = 23;   //11 PM
  const totalMinutes = (endHour - startHour) * 60;
  const elapsedMinutes = currentTime.getHours()*60 + currentTime.getMinutes() - startHour * 60;
  progressPercentage = (elapsedMinutes / totalMinutes) * 100;
  if (inverted) {
    progressPercentage = 100 - progressPercentage;
  }
  return progressPercentage;
}


let isCycleBarInverted = false;

function toggleCycleBar() {
  isCycleBarInverted = !isCycleBarInverted;
  updateNavCycleTimer();
  updateCycleProgressBar();
}

function updateNavCycleTimer() {                  
  if (end_time_str) {
      var end_time = new Date(end_time_str);
      var remaining = Math.floor((end_time - new Date()) / 1000);
      if (!isCycleBarInverted) {
        remaining = 99*60*60+59*60+59 - remaining;
      }
      var hours = Math.floor(remaining / 3600);
      var minutes = Math.floor((remaining % 3600) / 60).toString().padStart(2, '0');
      var seconds = (remaining % 60).toString().padStart(2, '0');
      var display = hours + ":" + minutes + ":" + seconds;
      UpdateStringTimer("nav_cycle_lbl_time", display );
  }
}


function calculateCycleProgressBarPercentage(inverted){
  var end_time = new Date(end_time_str);
  var remaining = Math.floor((end_time - new Date()) / 1000);
  let progressPercentage = remaining/3600;

  if (!inverted) {
    progressPercentage = 100 - progressPercentage;
  }
  return progressPercentage;
}



function updateCycleProgressBar() {
  const progressBar = document.getElementById('cycle-progress-bar');
  const progressText = document.getElementById('cycle_progress-text');
  progressPercentage = calculateCycleProgressBarPercentage(isCycleBarInverted);
  updateProgressBar(progressBar,progressText, progressPercentage, isCycleBarInverted );
}


function updateProgressBar(progressBar, progressText, progressPercentage, isInverted) {
    const progressBarInner = progressBar.querySelector('.progress-bar');
    let internal_label = "Elapsed: ";

    if (isInverted) {
        internal_label = "Remain: ";
    }

    if (progressPercentage < 5) {
      internal_label='';
    }
    
    if (progressPercentage < 0) {
        progressPercentage = 0;
    } else if (progressPercentage > 100) {
        progressPercentage = 100;
    }

    const progressPercentageFixed = progressPercentage.toFixed(0);
    progressBar.setAttribute('aria-valuenow', progressPercentageFixed);
    progressBarInner.style.width = `${progressPercentageFixed}%`;
    progressText.textContent = internal_label + ` ${progressPercentageFixed}%`;
}


function myFunction() {
  // add your desired functionality here
  console.log('Button clicked!');
}








