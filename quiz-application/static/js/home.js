function openNav() {
    console.log("Opening sidebar...");
    document.getElementById("main").style.marginLeft = "250px"; // Match the sidebar width
    document.getElementById("mySidebar").style.display = "block";
}

function closeNav() {
    console.log("Closing sidebar...");
    document.getElementById("main").style.marginLeft = "0";
    document.getElementById("mySidebar").style.display = "none";
}

// Initialize the sidebar state based on some condition or user action
// For example, if you want the sidebar to be open by default:
openNav(); // Open the sidebar by default

document.addEventListener('DOMContentLoaded', function() {
    console.log("Document loaded. Initializing...");

    const links = document.querySelectorAll('.category-link');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Function to handle sidebar link clicks
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default action
            console.log(`Link clicked: ${link.href}`);
            
            // Perform some action based on the link clicked
            // For example, changing the active state of the sidebar link
            link.classList.add('active'); // Assuming you have CSS for .active state
            // Remove 'active' class from all other links
            links.forEach(otherLink => {
                if (otherLink !== link) {
                    otherLink.classList.remove('active');
                }
            });

            // Extract category from URL and fetch questions
            const category = link.getAttribute('href').split('/').pop(); // Extract category from URL
            console.log(`Fetching questions for category: ${category}`);
            fetchQuestions(category);
        });
    });

    function fetchQuestions(category) {
        loadingIndicator.style.display = 'block';
        console.log(`Sending request to fetch questions for category: ${category}`);

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
            console.log('Received data:', data);
            if (data.error) {
                console.error('Error:', data.error);
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
        console.log('Questions displayed:', questions);
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
        console.log(`CSRF token retrieved: ${cookieValue}`);
        return cookieValue;
    }

    // Example of how to close the sidebar when clicking outside of it
    document.addEventListener('click', function(event) {
        var isClickInside = Array.from(document.getElementsByClassName('sidebar')).some(function(el) {
            return el.contains(event.target);
        });

        if (!isClickInside) {
            closeNav(); // Close the sidebar if the click was outside of it
        }
    });

    console.log("Initialization complete.");
});
