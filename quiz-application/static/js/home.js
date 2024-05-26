function openNav() {
    document.getElementById("main").style.marginLeft = "250px"; // Match the sidebar width
    document.getElementById("mySidebar").style.display = "block";
}

function closeNav() {
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("mySidebar").style.display = "none";
}

// Initialize the sidebar state based on some condition or user action
// For example, if you want the sidebar to be open by default:
openNav(); // Open the sidebar by default

document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.category-link');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Function to handle sidebar link clicks
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default action
            // Perform some action based on the link clicked
            // For example, changing the active state of the sidebar link
            link.classList.add('active'); // Assuming you have CSS for.active state
            // Remove 'active' class from all other links
            links.forEach(otherLink => {
                if (otherLink!== link) {
                    otherLink.classList.remove('active');
                }
            });

            // Optionally, perform some action based on the link clicked
            // For example, filtering content displayed in the main content area
            // This depends on your application's requirements
        });
    });

    // Hide the loading indicator since we're not fetching content dynamically anymore
    loadingIndicator.style.display = 'none';
});

// Example of how to close the sidebar when clicking outside of it
document.addEventListener('click', function(event) {
    var isClickInside = Array.from(document.getElementsByClassName('sidebar')).some(function(el) {
        return el.contains(event.target);
    });

    if (!isClickInside) {
        closeNav(); // Close the sidebar if the click was outside of it
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const links = document.querySelectorAll('.category-link');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Function to handle sidebar link clicks
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default action
            const category = link.getAttribute('href').split('/').pop(); // Extract category from URL
            fetchQuestions(category);
        });
    });

    function fetchQuestions(category) {
        loadingIndicator.style.display = 'block';

        fetch('/fetch_questions/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') // Ensure CSRF token is included
            },
            body: JSON.stringify({ category: category })
        })
        .then(response => response.json())
        .then(data => {
            loadingIndicator.style.display = 'none';
            if (data.error) {
                console.error(data.error);
            } else {
                displayQuestions(data.questions);
            }
        })
        .catch(error => {
            loadingIndicator.style.display = 'none';
            console.error('Error fetching questions:', error);
        });
    }

    function displayQuestions(questions) {
        const contentArea = document.getElementById('content-area');
        contentArea.innerHTML = ''; // Clear previous content

        questions.forEach(q => {
            const questionDiv = document.createElement('div');
            questionDiv.classList.add('question');
            questionDiv.innerHTML = `
                <h4>${q.question}</h4>
                <ul>
                    <li>${q.option1}</li>
                    <li>${q.option2}</li>
                    <li>${q.option3}</li>
                    <li>${q.option4}</li>
                </ul>
            `;
            contentArea.appendChild(questionDiv);
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Open the sidebar by default
    openNav();
});
