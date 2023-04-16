let isCurrentCycleActiveVar = false;
let internal_cycle_end_time_str;

document.addEventListener('DOMContentLoaded', function () {
    isCurrentCycleActiveVar = isCurrentCycleActive();
    manageCycleElements(isCurrentCycleActiveVar);
    const nav_cycle_time_lbl = document.getElementById('nav_cycle_lbl_time');
    nav_cycle_time_lbl.addEventListener('click', toggleCycleBar);

    updateNavCycleTimer();
    updateCycleProgressBar();
    updatePeriodicData();
  });

function isCurrentCycleActive() 
{
  if (current_cycle_obj == "None")
    return false;
  updateInternalVariables(current_cycle_obj);
  return true;
}

function manageCycleElements (isCurrentCycleActiveVar)
{
  const cycle_progressBar = document.getElementById('cycle-progress-bar');
  const cycle_startButton = document.getElementById('cycle-start-button');

  if (!isCurrentCycleActiveVar) {
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

function updatePeriodicData () { 
  setInterval(updateCycleProgressBar, 60000);
  setInterval(updateNavCycleTimer, 500);
}

function updateInternalVariables(json_obj)
{
  var current_cycle = JSON.parse(json_obj);
  var start_time = current_cycle.start_time;
  var end_time = current_cycle.end_time;
  internal_cycle_end_time_str = end_time;
}


let isCycleBarInverted = true;
function toggleCycleBar() {
  isCycleBarInverted = !isCycleBarInverted;
  updateNavCycleTimer();
  updateCycleProgressBar();
}

function updateNavCycleTimer() {                  
  if (internal_cycle_end_time_str) {
      var end_time = new Date(internal_cycle_end_time_str);
      var remaining = Math.floor((end_time - new Date()) / 1000);
      if (!isCycleBarInverted) {
        remaining = 99*60*60+59*60+59 - remaining;
      }
      remaining = remaining < 0?0:remaining;
      var hours = Math.floor(remaining / 3600);
      var minutes = Math.floor((remaining % 3600) / 60).toString().padStart(2, '0');
      var seconds = (remaining % 60).toString().padStart(2, '0');
      var display = hours + ":" + minutes + ":" + seconds;
      UpdateStringTimer("nav_cycle_lbl_time", display );
  }
}

function calculateCycleProgressBarPercentage(inverted)
{
  var end_time = new Date(internal_cycle_end_time_str);
  var remaining = Math.floor((end_time - new Date()) / 1000);
  let progressPercentage = remaining/3600;

  if (!inverted) {
    progressPercentage = 100 - progressPercentage;
  }
  return progressPercentage;
}

function updateCycleProgressBar()
{
  const progressBar = document.getElementById('cycle-progress-bar');
  const progressText = document.getElementById('cycle_progress-text');
  progressPercentage = calculateCycleProgressBarPercentage(isCycleBarInverted);
  updateProgressBar(progressBar,progressText, progressPercentage, isCycleBarInverted );
}

async function StartCycle() {
  const csrfToken = djangoCycleData.csrfToken;
  const requestOptions = {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
      }
  };

  try {
      const response = await fetch(djangoCycleData.createCycleUrl, requestOptions);
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data = await response.json();
      manageCycleElements(true);
      updateInternalVariables(data.current_cycle);
      updateNavCycleTimer();
      updateCycleProgressBar();
      updatePeriodicData();

  } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
      alert('Error creating object');
  }
}





