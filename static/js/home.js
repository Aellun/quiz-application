document.addEventListener('DOMContentLoaded', function() {
    console.log("Document loaded. Initializing...");

    function openNav() {
        const mainElement = document.getElementById("main");
        const sidebarElement = document.getElementById("mySidebar");
        
        if (mainElement && sidebarElement) {
            console.log("Opening sidebar...");
            mainElement.style.marginLeft = "250px"; // Match the sidebar width
            sidebarElement.style.display = "block";
        } else {
            console.error("Element not found: #main or #mySidebar");
        }
    }
    
    function closeNav() {
        const mainElement = document.getElementById("main");
        const sidebarElement = document.getElementById("mySidebar");

        if (mainElement && sidebarElement) {
            console.log("Closing sidebar...");
            mainElement.style.marginLeft = "0";
            sidebarElement.style.display = "none";
        } else {
            console.error("Element not found: #main or #mySidebar");
        }
    }
    
    // Initialize the sidebar state based on some condition or user action
    openNav(); // Open the sidebar by default

    const links = document.querySelectorAll('.category-link');
    const loadingIndicator = document.getElementById('loading-indicator');

    // Function to handle sidebar link clicks
    links.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default action
            console.log(`Link clicked: ${link.href}`);
            
            // Perform some action based on the link clicked
            link.classList.add('active'); // Assuming you have CSS for.active state
            // Remove 'active' class from all other links
            links.forEach(otherLink => {
                if (otherLink!== link) {
                    otherLink.classList.remove('active');
                }
            });
            
            // Extract category from URL and fetch questions
    //         const category = link.getAttribute('href').split('/').slice(-2).join('/');
    //         console.log(`Extracted category from URL: ${category}`);
    //         if (category) {
    //             fetchQuestions(category);
    //         } else {
    //             console.error('Category is empty.');
    //         }
    //     });
    // });

    document.querySelectorAll('.category-link').forEach(link => {
        link.addEventListener('click', event => {
            event.preventDefault(); // Prevent navigation
    
            const categoryLink = event.target.href.split('/').pop();
            const form = document.querySelector('#category-form'); // Target the form by its ID
            const selectedCategoryInput = form.querySelector('#selected-category');
    
            selectedCategoryInput.value = categoryLink; // Set the selected category
            form.style.display = 'block'; // Make the form visible
            form.submit(); // Submit the form
        });
    });
    

    function fetchQuestions(category) {
        if (loadingIndicator) {
            loadingIndicator.style.display = 'block';
            console.log(`Sending request to fetch questions for category: ${category}`);
    
            // Log the request details
            console.log(`Request URL: http://127.0.0.1:8000/fetch_questions/`);
            console.log(`Request Method: POST`);
    
            // Log the headers
            console.log(`Headers:`);
            console.log(`Content-Type: application/json`);
            console.log(`X-CSRFToken: ${getCookie('csrftoken')}`); // Assuming getCookie is a function that retrieves the CSRF token
    
            // Log the body
            console.log(`Body:`, JSON.stringify({ category: category }));
    
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
                if (loadingIndicator) {
                    loadingIndicator.style.display = 'none';
                }
                console.log('Received data:', data);
                if (data.error) {
                    console.error('Error:', data.error);
                } else {
                    displayQuestions(data.questions);
                }
            })
          .catch(error => {
                if (loadingIndicator) {
                    loadingIndicator.style.display = 'none';
                }
                console.error('Error fetching questions:', error);
            });
        } else {
            console.error("Loading indicator not found");
        }
    }
    

    function displayQuestions(questions) {
        const contentArea = document.getElementById('content-area');
        if (contentArea) {
            contentArea.innerHTML = ''; // Clear previous content
            console.log('Displaying questions:', questions);
    
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
        } else {
            console.error("Content area not found");
        }
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie!== '') {
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
