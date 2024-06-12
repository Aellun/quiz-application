from django.apps import AppConfig

class QuizConfig(AppConfig):
    name = 'Quiz'

    def ready(self):
        import Quiz.signals
