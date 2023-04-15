document.addEventListener('DOMContentLoaded', function () {

    manageCycleElements(cycle);
    const nav_cycle_time_lbl = document.getElementById('nav_cycle_lbl_time');
    nav_cycle_time_lbl.addEventListener('click', toggleCycleBar);

    updateNavCycleTimer();
    updateCycleProgressBar();
    updatePeriodicData();
  });



function updatePeriodicData () { 
  setInterval(updateCycleProgressBar, 60000);
  setInterval(updateNavCycleTimer, 500);
}


let isCycleBarInverted = false;

function toggleCycleBar() {
  isCycleBarInverted = !isCycleBarInverted;
  updateNavCycleTimer();
  updateCycleProgressBar();
}

function updateNavCycleTimer() {                  
  if (cycle_end_time_str) {
      var end_time = new Date(cycle_end_time_str);
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
  var end_time = new Date(cycle_end_time_str);
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

  function manageCycleElements (cycle){
    const cycle_progressBar = document.getElementById('cycle-progress-bar');
    const cycle_startButton = document.getElementById('cycle-start-button');
    if (cycle == "None") {
      cycle_startButton.style.display = "block";      
      cycle_progressBar.style.display = "none";
      cycle_progressBar.addEventListener('click', toggleCycleBar);
    }
    else {
      cycle_startButton.style.display = "none";      
      cycle_progressBar.style.display = "block";
      cycle_progressBar.addEventListener('click', toggleCycleBar);
    }
  }









