document.addEventListener("DOMContentLoaded", function() {
    console.log("page loaded");

    const startTime = djangoData.startTime;

    if (startTime) {
        startChronometer(startTime);
        const createObjectButton = document.getElementById('create-object-btn');
        createObjectButton.innerHTML = "Stop Cycle";
        createObjectButton.removeEventListener('click', StartCycle);
        createObjectButton.addEventListener('click', StopCycle);
    }
    else {
        const createObjectButton = document.getElementById('create-object-btn');
        createObjectButton.innerHTML = "Start Cycle";
        createObjectButton.removeEventListener('click', StopCycle);
        createObjectButton.addEventListener('click', StartCycle);
    }
    
});

function formatTime(timeInSeconds) {
    const hours = Math.floor(timeInSeconds / 3600);
    const minutes = Math.floor((timeInSeconds - (hours * 3600)) / 60);
    const seconds = timeInSeconds % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

function startChronometer(startTime) {
    const startTimestamp = startTime * 1000;
    const now = new Date().getTime();
    const elapsedTime = Math.floor((now - startTimestamp) / 1000);
    const chronometer = document.getElementById('chronometer');
    chronometer.textContent = formatTime(elapsedTime);

    setInterval(() => {
        const now = new Date().getTime();
        const elapsedTime = Math.floor((now - startTimestamp) / 1000);
        chronometer.textContent = formatTime(elapsedTime);
    }, 1000);
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
        const objectContainer = document.getElementById('object-container');
        objectContainer.innerHTML = '<p id="object-text">' + data.text + '</p><span id="chronometer">00:00:00</span>';
        
        const startTimeContainer = document.getElementById('start-time-container');
        startTimeContainer.innerHTML = `<p>Start Time: ${data.formatted_local_start_time}</p>`;

        startChronometer(data.start_time);
        const createObjectButton = document.getElementById('create-object-btn');
        createObjectButton.innerHTML = "Stop Cycle";
        createObjectButton.removeEventListener('click', StartCycle);
        createObjectButton.addEventListener('click', StopCycle);
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
        const objectContainer = document.getElementById('object-container');
        objectContainer.innerHTML = '';
        const createObjectButton = document.getElementById('create-object-btn');
        createObjectButton.innerHTML = "Start Cycle";
        createObjectButton.removeEventListener('click', StopCycle);
        createObjectButton.addEventListener('click', StartCycle);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert('Error creating object');
    }
}




