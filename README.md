# LearnHub

Welcome to LearnHub, a web-based application designed to provide employees with self-development tools and resources within organizations. LearnHub aims to empower growth and nurture talent by offering a flexible and convenient online platform for skill development.

### Live Demo
Experience LearnHub in action by visiting our [Live Demo](https://learnhub-seven.vercel.app/).

### Blog Article
Read more about the journey and development of LearnHub in our [Project Blog](https://medium.com/@allankevin22/7e52eb226d42).

### Author
**Okello Kevin**
- LinkedIn: [Okello Kevin](https://github.com/Aellun)

## Architecture
LearnHub uses HTML, CSS, and JavaScript for the frontend to create a responsive and user-friendly interface. The backend is powered by Django, which handles application logic, user authentication, and routing. PostgreSQL is used for the database, hosted on Amazon RDS for reliability and scalability. The application follows the Model-View-Template (MVT) architecture pattern provided by Django, ensuring a clear separation of concerns and maintainability.

## Installation and Usage
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

4. **Create a superuser:**
   ```sh
   python manage.py createsuperuser

5. **Run the server:**
   ```sh
   python manage.py runserver

6. **Access the application:**
   Open your browser and navigate to http://localhost:8000.

## Usage
- **Landing Page:** Visit the landing page to learn more about LearnHub and its features.
- **User Registration:** New users can register for an account by providing their details.
- **User Login:** Registered users can log in to access their personalized dashboard.
- **Dashboard:** Users can access various quizzes and resources for self-development.
- **Add Questions:** Admin users can add new quiz questions to the platform.

## Contributing
We welcome contributions! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/your-feature

3. Commit your changes:
   ```sh
   git commit -m 'Add some feature'

4. Push to the branch:
   ```sh
   git push origin feature/your-feature

5. Open a pull request.

## Related Projects
- **QuizHub:** An open-source quiz platform.
- **SelfDev:** A web-based application for personal development.

## Bugs and Continuous Development
LearnHub is my first active project, and it has been a significant learning experience. Some ongoing issues include:

- User feedback on login or registration is not yet active.
- Quiz buttons are not yet embedded on the courses.

LearnHub is in continuous development, and your feedback and contributions are highly appreciated as we strive to improve its functionality and user experience.

## Licensing
This project is not yet licensed.

Thank you for your interest in LearnHub!
