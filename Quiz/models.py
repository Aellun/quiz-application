from django.db import models
from django.contrib.auth.models import User

class QuesModel(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Computer Science'),
        ('communication', 'Communication Skills'),
        ('emotion', 'Emotional Intelligence'),
        ('ethics', 'Ethics'),
        ('sales', 'Customer Service'),
        # Add more categories as needed
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200, default='Option 1')
    option2 = models.CharField(max_length=200, default='Option 2')
    option3 = models.CharField(max_length=200, default='Option 3')
    option4 = models.CharField(max_length=200, default='Option 4')
    
    OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    
    answer = models.CharField(max_length=50, choices=OPTION_CHOICES, default='option1')
    
    def __str__(self):
        return self.question


class QuizAttempt(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='quizzes_taken')
    category = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.category} - {self.score}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.IntegerField(default=0)
    num_tests_taken = models.IntegerField(default=0)

    def calculate_average_score(self):
        return self.total_score / self.num_tests_taken if self.num_tests_taken else 0