# LearnHub

## Introduction
Welcome to LearnHub, a web-based application designed to provide employees with self-development tools and resources within organizations. LearnHub aims to empower growth and nurture talent by offering a flexible and convenient online platform for skill development.

### Live Demo
Experience LearnHub in action by visiting our [Live Demo](learnhub-seven.vercel.app/).

### Blog Article
Read more about the journey and development of LearnHub in our [Project Blog](https://medium.com/@allankevin22/7e52eb226d42 ).

### Author
**Okello Kevin**
- LinkedIn: [Okello Kevin](https://github.com/Aellun)

Architecture
Frontend
The frontend of LearnHub is built using HTML, CSS, and JavaScript. The goal is to create a responsive and user-friendly interface that works seamlessly across different devices. Key components include:

HTML: Structure of the web pages.
CSS: Styling and layout, ensuring the application is visually appealing and responsive.
JavaScript: Enhancing interactivity, such as handling form submissions and dynamic content loading.
Backend
The backend of LearnHub is powered by Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design. Key components include:

Django: Handles the application logic, user authentication, and routing.
PostgreSQL: The database system used to store user data, quiz questions, and results.
Amazon RDS: Hosting the PostgreSQL database, ensuring reliability and scalability.
REST API: Used for communication between the frontend and backend, particularly for fetching quiz questions and submitting answers.
The application follows the Model-View-Template (MVT) architecture pattern provided by Django, ensuring a clear separation of concerns and making the codebase more maintainable.

## Installation
To run LearnHub locally, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Aellun/quiz-application.git
   cd LearnHub

2. **Install dependencies:**
     ```sh
   pip install -r requirements.txt

3. **Set up the database:**
     ```sh
    python manage.py migrate

 4.   **Create a superuser:**

 ```sh
python manage.py createsuperuser


5. **Run the server:**

 ```sh
python manage.py runserver


6. **Access the application:**
Open your browser and navigate to http://localhost:8000.

Usage
Landing Page
Visit the landing page to learn more about LearnHub and its features.

User Registration
New users can register for an account by providing their details.

User Login
Registered users can log in to access their personalized dashboard.

Dashboard
Users can access various quizzes and resources for self-development.

Add Questions
Admin users can add new quiz questions to the platform.

Contributing
We welcome contributions! To contribute, please follow these steps:

Fork the repository.
Create a new branch:
sh
Copy code
git checkout -b feature/your-feature
Commit your changes:
sh
Copy code
git commit -m 'Add some feature'
Push to the branch:
sh
Copy code
git push origin feature/your-feature
Open a pull request.

Related Projects
QuizHub: An open-source quiz platform.
SelfDev: A web-based application for personal development.

Bugs
LearnHub is my first active project, and it has been a significant learning experience
one of them is that the user feedback on login or registration are not yet active
the quiz buttons are not ye embedded on the courses yet
LearnHub is in continuous development, and your feedback and contributions are highly appreciated as we strive to improve its functionality and user experience.

Licensing
This project is not yet licensed

Thank you for your interest in LearnHub!