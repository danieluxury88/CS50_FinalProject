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


function updateTimer(element_id, timer) {
  const hours = timer.getHours();
  const minutes = timer.getMinutes();
  const seconds = timer.getSeconds();
  const timeString = `${hours}:${padZero(minutes)}:${padZero(seconds)}`;
  UpdateStringTimer(element_id,timeString );
}

function formatStartTime(dateTimeString) {
  const date = new Date(dateTimeString);
  let hours = date.getHours();
  let minutes = date.getMinutes();
  const ampm = hours >= 12 ? 'p.m.' : 'a.m.';
  hours = hours % 12;
  hours = hours ? hours : 12;
  minutes = minutes < 10 ? '0' + minutes : minutes;
  return hours + ':' + minutes + ' ' + ampm;
}

function padZero(number) {
  return number < 10 ? "0" + number : number;
}

function UpdateStringTimer(element_id, timeString ) {
  document.getElementById(element_id).innerHTML = timeString;
}


function formatTime(timeInSeconds) {
  const hours = Math.floor(timeInSeconds / 3600);
  const minutes = Math.floor((timeInSeconds - (hours * 3600)) / 60);
  const seconds = timeInSeconds % 60;
  return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}


function startChronometer(startTime, chronometerID) {
  const startTimestamp = startTime * 1000;
  const now = new Date().getTime();
  const elapsedTime = Math.floor((now - startTimestamp) / 1000);
  const chronometer = document.getElementById(chronometerID);
  chronometer.textContent = formatTime(elapsedTime);

  intervalId = setInterval(() => {
      const now = new Date().getTime();
      const elapsedTime = Math.floor((now - startTimestamp) / 1000);
      chronometer.textContent = formatTime(elapsedTime);
  }, 1000);

  return intervalId;
}

function stopChronometer(intervalId) {
  clearInterval(intervalId);
}


function myFunction() {
  // add your desired functionality here
  console.log('Button clicked!');
}


function viewTask(taskId) {
    console.log(taskId);
    // Get the list item element
    const listItem = document.querySelector(`[data-url*="tasks/task_update/${taskId}/"]`);

    // Get the URL from the data-url attribute
    const url = listItem.getAttribute('data-url');

    // Navigate to the URL
    window.location.href = url;
}

