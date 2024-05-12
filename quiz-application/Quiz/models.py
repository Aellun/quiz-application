from django.db import models

class QuesModel(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('communication', 'Communication'),
        ('Emotion', 'Emotion'),
        ('Ethics', 'Ethics'),
        ('Sales', 'Sales')
        ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    question = models.CharField(max_length=200, null=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)
    option4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.question
