document.addEventListener("DOMContentLoaded", function() {

    const startTime = djangoData.startTime;

    const workSessionContainer = document.getElementById('worksession-container');
    if (startTime) {
        workSessionContainer.style.display = "block";    
        startChronometer(startTime);
        const startWorkCycleButton = document.getElementById('start-work-cycle-btn');
        startWorkCycleButton.innerHTML = "Stop Cycle";
        startWorkCycleButton.removeEventListener('click', StartCycle);
        startWorkCycleButton.addEventListener('click', StopCycle);
    }
    else {
        workSessionContainer.style.display = "none"; 
        const startWorkCycleButton = document.getElementById('start-work-cycle-btn');
        startWorkCycleButton.innerHTML = "Start Cycle";
        startWorkCycleButton.removeEventListener('click', StopCycle);
        startWorkCycleButton.addEventListener('click', StartCycle);
    }
    
});

function formatTime(timeInSeconds) {
    const hours = Math.floor(timeInSeconds / 3600);
    const minutes = Math.floor((timeInSeconds - (hours * 3600)) / 60);
    const seconds = timeInSeconds % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

let intervalId;

function startChronometer(startTime) {
    const startTimestamp = startTime * 1000;
    const now = new Date().getTime();
    const elapsedTime = Math.floor((now - startTimestamp) / 1000);
    const chronometer = document.getElementById('chronometer');
    chronometer.textContent = formatTime(elapsedTime);

    intervalId = setInterval(() => {
        const now = new Date().getTime();
        const elapsedTime = Math.floor((now - startTimestamp) / 1000);
        chronometer.textContent = formatTime(elapsedTime);
    }, 1000);

    return intervalId;
}

function stopChronometer() {
    clearInterval(intervalId);
}


async function StartCycle() {
    const csrfToken = djangoData.csrfToken;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    };
    try {
        const response = await fetch(djangoData.startCycleUrl, requestOptions);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();

        const workSessionStartTime = document.getElementById('work_session_start_time');
        workSessionStartTime.innerHTML = `${data.formatted_local_start_time}`;

        const workSessionContainer = document.getElementById('worksession-container');
        workSessionContainer.style.display = 'block';

        
        startChronometer(data.start_time);
        const startWorkCycleButton = document.getElementById('start-work-cycle-btn');
        startWorkCycleButton.innerHTML = "Stop Cycle";
        startWorkCycleButton.removeEventListener('click', StartCycle);
        startWorkCycleButton.addEventListener('click', StopCycle);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert('Error creating object');
    }
}


async function StopCycle() {
    const csrfToken = djangoData.csrfToken;
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    };
    try {
        const response = await fetch(djangoData.stopCycleUrl, requestOptions);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        const workSessionContainer = document.getElementById('worksession-container');
        workSessionContainer.style.display = 'none';
        const startWorkCycleButton = document.getElementById('start-work-cycle-btn');
        startWorkCycleButton.innerHTML = "Start Cycle";
        startWorkCycleButton.removeEventListener('click', StopCycle);
        startWorkCycleButton.addEventListener('click', StartCycle);
        stopChronometer();
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert('Error creating object');
    }
}




