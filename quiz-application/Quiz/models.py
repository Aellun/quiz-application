from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    option1 = models.CharField(max_length=200,null=True)
    option2 = models.CharField(max_length=200,null=True)
    option3 = models.CharField(max_length=200,null=True)
    option4 = models.CharField(max_length=200,null=True)
    answer = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question