document.addEventListener('DOMContentLoaded', function() {
    console.log("Document loaded. Initializing...");

    // Function to open the sidebar
    function openNav() {
        const mainElement = document.getElementById("main");
        const sidebarElement = document.getElementById("mySidebar");
        
        if (mainElement && sidebarElement) {
            console.log("Opening sidebar...");
            mainElement.style.marginLeft = "250px"; // Adjust main content margin
            sidebarElement.style.display = "block";
            document.getElementById("sidebarToggle").innerHTML = "&gt;"; // Update button to indicate sidebar is open
        } else {
            console.error("Element not found: #main or #mySidebar");
        }
    }
    
    // Function to close the sidebar
    function closeNav() {
        const mainElement = document.getElementById("main");
        const sidebarElement = document.getElementById("mySidebar");

        if (mainElement && sidebarElement) {
            console.log("Closing sidebar...");
            mainElement.style.marginLeft = "0"; // Reset main content margin
            sidebarElement.style.display = "none";
            document.getElementById("sidebarToggle").innerHTML = "&lt;"; // Update button to indicate sidebar is closed
        } else {
            console.error("Element not found: #main or #mySidebar");
        }
    }
    
    // Function to toggle the sidebar
    function toggleSidebar() {
        const sidebarElement = document.getElementById("mySidebar");
        if (sidebarElement.style.display === "none") {
            openNav(); // Show the sidebar
        } else {
            closeNav(); // Hide the sidebar
        }
    }

    // Initialize the sidebar state based on some condition or user action
    // For demonstration, the sidebar is opened by default
    openNav();

    // Get references to the sidebar toggle button and the sidebar itself
    const toggleButton = document.getElementById("sidebarToggle"); // Ensure this ID matches your HTML
    const sidebar = document.getElementById("mySidebar");

    // Attach the toggle function to the button's click event
    toggleButton.addEventListener('click', toggleSidebar);

    console.log("Initialization complete.");
});
