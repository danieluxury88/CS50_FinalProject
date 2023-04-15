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

function padZero(number) {
  return number < 10 ? "0" + number : number;
}

function UpdateStringTimer(element_id, timeString ) {
  document.getElementById(element_id).innerHTML = timeString;
}


function myFunction() {
  // add your desired functionality here
  console.log('Button clicked!');
}

