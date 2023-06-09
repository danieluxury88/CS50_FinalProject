// A function to retrieve CSRF token from cookies
const getCSRFToken = () => {
    const cookies = document.cookie.split(";");
    const csrfToken = cookies.find(cookie => cookie.trim().startsWith("csrftoken="));
    return csrfToken ? csrfToken.trim().substring("csrftoken=".length) : "";
}

// A function to handle click event
const handleClick = (event) => {
    event.preventDefault();

    const webAddress = event.currentTarget.href;
    const csrfToken = getCSRFToken();
    
    const data = {
        'download_link': webAddress
    };

    fetch('register-download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify(data),
    })
    .then((response) => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        window.open(webAddress, '_blank');
    })
    .catch((error) => {
        console.error('There has been a problem with your fetch operation:', error);
    });
}

// Get all elements with class js-download-link and attach event listener to each of the links
Array.from(document.getElementsByClassName('js-download-link')).forEach(link => {
    link.addEventListener('click', handleClick);
});