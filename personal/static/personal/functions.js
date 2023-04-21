document.addEventListener('DOMContentLoaded', function () {
    startWorkSessionTimer();
    updateTimers();
  });


function updateCycleTimer() {
    var end_time = new Date(end_time_str);
    var remaining = Math.floor((end_time - new Date()) / 1000);
    var hours = Math.floor(remaining / 3600);
    var minutes = Math.floor((remaining % 3600) / 60).toString().padStart(2, '0');
    var seconds = (remaining % 60).toString().padStart(2, '0');
    var display = hours + ":" + minutes + ":" + seconds;
    document.getElementById("time-remaining").textContent = display;

}

function updateWorkSessionTimer() {
    if (current_session_start_str) {
        console.log("Active Work session")
        var current_session_start = new Date(current_session_start_str);
        var current_session_duration = Math.floor((new Date() - current_session_start) / 1000);
        var hours = Math.floor(current_session_duration / 3600);
        var minutes = Math.floor((current_session_duration % 3600) / 60).toString().padStart(2, '0');
        var seconds = (current_session_duration % 60).toString().padStart(2, '0');
        var display = hours + ":" + minutes + ":" + seconds;
        document.getElementById("current_work_session_duration").textContent = display;

    }
}

function startWorkSessionTimer() {
    ctrl_work_session_btn = document.getElementById("ctrl_work_session")
    ctrl_work_session_btn.addEventListener('click', () => toggleWorkingSession());
    if (current_session_start_str) {
        ctrl_work_session_btn.innerHTML="Stop";
        updateWorkSessionTimer();
    }
    else {
        ctrl_work_session_btn.innerHTML="Start";
    }

}

function updateTimers() {
    updateCycleTimer();
    updateWorkSessionTimer();    
    setInterval(updateTimers, 450);
}



// .then(response => {
//     if (response.ok) {
//       // Update the end time in the HTML DOM.
//       console.log("Ok")
//     } else {
//       throw new Error('WorkSession update failed.');
//     }
//   })
//   .then(()=> startWorkSessionTimer())
//   .catch(error => {
//     console.error(error);
//   });