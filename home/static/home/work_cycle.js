document.addEventListener("DOMContentLoaded", function() {

    const workSessionStartTime = djangoData.workSessionStartTime;

    const workSessionContainer = document.getElementById('work_session-container');
    if (workSessionStartTime) {
        workSessionContainer.style.display = "block";    
        startWorkSessionChronometer(workSessionStartTime, 'work_session_chronometer');
        configureWorkSessionButton("Stop");
    }
    else {
        workSessionContainer.style.display = "none";
        configureWorkSessionButton("Start");
    }
    
});

function configureWorkSessionButton ( state )
{
    const startWorkCycleButton = document.getElementById('start-work-cycle-btn');
    if (state == "Start") {
        startWorkCycleButton.innerHTML = "Start Work Session";
        startWorkCycleButton.removeEventListener('click', StopWorkSession);
        startWorkCycleButton.addEventListener('click', StartWorkSession);
        startWorkCycleButton.classList.remove("btn-danger");
        startWorkCycleButton.classList.add("btn-success");
    }
    else if (state == "Stop") {
        startWorkCycleButton.innerHTML = "Stop Work Session";
        startWorkCycleButton.removeEventListener('click', StartWorkSession);
        startWorkCycleButton.addEventListener('click', StopWorkSession);
        startWorkCycleButton.classList.add("btn-danger");
        startWorkCycleButton.classList.remove("btn-success");
    }
}

let workSessionIntervalId;

function startWorkSessionChronometer(workSessionStartTime){
    workSessionIntervalId = startChronometer(workSessionStartTime, 'work_session_chronometer');
}

function stopWorkSessionChronometer(){
    stopChronometer(workSessionIntervalId);
}


async function StartWorkSession() {
    const csrfToken = djangoData.csrfToken;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    };
    try {
        const response = await fetch(djangoData.startWorkSessionUrl, requestOptions);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();

        const workSessionStartTime = document.getElementById('work_session_start_time');
        workSessionStartTime.innerHTML = `${data.formatted_local_start_time}`;

        const workSessionContainer = document.getElementById('work_session-container');
        workSessionContainer.style.display = 'block';

        
        startWorkSessionChronometer(data.start_time, 'work_session_chronometer');
        configureWorkSessionButton("Start");

    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert('Error creating object');
    }
}


async function StopWorkSession() {
    const csrfToken = djangoData.csrfToken;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    };
    try {
        const response = await fetch(djangoData.stopWorkSessionUrl, requestOptions);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        const workSessionContainer = document.getElementById('work_session-container');
        workSessionContainer.style.display = 'none';
        configureWorkSessionButton("Start");
        stopWorkSessionChronometer();
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert('Error creating object');
    }
}




