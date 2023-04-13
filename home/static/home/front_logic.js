document.addEventListener('DOMContentLoaded', function () {
    const progressBar = document.getElementById('day-progress-bar');
    progressBar.addEventListener('click', toggleInverted);

    btn_toggle_work_session.onclick = toggleWorkingSession  

    updateNavClock();
    updateAuxClock();
    updateDayProgressBar();
    updatePeriodicData();

  });


function toggleWorkingSession(){
  event.preventDefault();
  console.log("button");
  fetch(`personal/toggle_work_session/` , {
      method: 'GET',
  });
}

function updateTimer(element_id, timer) {
  const hours = timer.getHours();
  const minutes = timer.getMinutes();
  const seconds = timer.getSeconds();
  const timeString = `${hours}:${padZero(minutes)}:${padZero(seconds)}`;
  document.getElementById(element_id).innerHTML = timeString;
}

function padZero(number) {
  return number < 10 ? "0" + number : number;
}

function updateNavClock() {
  var now = new Date();
  updateTimer("nav_clock", now );
}

function updateAuxClock() {
  var now = new Date();
  updateTimer("timer", now );
}

function updatePeriodicData () { 
  setInterval(updateNavClock, 1000);
  setInterval(updateAuxClock, 1000);
  setInterval(updateDayProgressBar, 60000);
}

function myFunction() {
  // add your desired functionality here
  console.log('Button clicked!');
}

// 


let isDayBarInverted = false;

function updateDayProgressBar() {
  const progressBar = document.getElementById('day-progress-bar');
  const progressText = document.getElementById('day_progress-text');
  updateProgressBar(progressBar,progressText, isDayBarInverted )
}

function toggleInverted() {
  isDayBarInverted = !isDayBarInverted;
  updateDayProgressBar();
}

            
function updateProgressBar(progressBar, progressText, isInverted) {
    const progressBarInner = progressBar.querySelector('.progress-bar');

    const currentTime = new Date();
    const startHour = 5; // 6 AM
    const endHour = 22; // 10 PM

    const totalMinutes = (endHour - startHour) * 60;
    const elapsedMinutes = currentTime.getHours()*60 + currentTime.getMinutes() - startHour * 60;


    let progressPercentage = (elapsedMinutes / totalMinutes) * 100;
    let internal_label = "Elapsed: ";

    if (isInverted) {
        progressPercentage = 100 - progressPercentage;
        internal_label = "Remain: ";
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






