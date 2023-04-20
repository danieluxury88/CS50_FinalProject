function RegisterEvent(event_type) {
    const csrfToken = getCSRFToken();

    fetch(`personal/test-register-event/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({event_type: event_type}),
    })
    .then(response => response.json())
    .then(data => {
        console.log("data", data);
        const event = JSON.parse(data.event)[0];
        const timeFormatted = formatStartTime(event.fields.date);
        const title = event.fields.title;
        const eventElement = `
        <li class="list-group-item d-flex justify-content-between align-items-start">
            <div class="container">
                <div class="row">
                    <div class="col-md-8">
                        <div class="fw-bold">
                            ${title} 
                        </div>
                            ${timeFormatted}
                    </div>
                </div>
            </div>
        </li>
        `
        document.getElementById(`event-list-${event_type}`).insertAdjacentHTML("beforeend", eventElement);
        currentVal = document.getElementById(`event-counter-${event_type}`).innerHTML;
        currentVal++;
        document.getElementById(`event-counter-${event_type}`).innerHTML = currentVal;
    })
    .catch(error => {
        console.error("Error creating work session:", error);
    });
}

function getCSRFToken() {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
            return cookie.substring("csrftoken=".length, cookie.length);
        }
    }
    return "";
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
