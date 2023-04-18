// work_sessions.js
document.addEventListener("DOMContentLoaded", function() {
    let endTimeModal;

    document.getElementById("create-work-session").addEventListener("click", function() {
        endTimeModal = new bootstrap.Modal(document.getElementById('end-time-modal'));
        endTimeModal.show();
    });

    document.getElementById("save-end-time").addEventListener("click", function() {
        const endTime = document.getElementById("end-time-input").value;
        createWorkSession(endTime);
        endTimeModal.hide();
    });

    function createWorkSession(endTime) {
        const csrfToken = getCSRFToken();

        fetch(``, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken,
            },
            body: JSON.stringify({end_time: endTime}),
        })
        .then(response => response.json())
        .then(data => {
            const workSession = JSON.parse(data.work_session)[0];
            const startTimeFormatted = formatStartTime(workSession.fields.start_time);
            const endTimeFormatted = formatStartTime(workSession.fields.end_time);
            const newWorkSession = `<li id="work-session-${workSession.pk}">Work Session ${workSession.pk} - Start Time: ${startTimeFormatted} - End Time: ${endTimeFormatted}</li>`
            document.getElementById("work-session-list").insertAdjacentHTML("beforeend", newWorkSession);
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
        hours = hours ? hours : 12; // the hour '0' should be '12'
        minutes = minutes < 10 ? '0' + minutes : minutes;
        return hours + ':' + minutes + ' ' + ampm;
    }
});
