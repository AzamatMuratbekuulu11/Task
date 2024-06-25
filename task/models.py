from django.db import models

class Task(models.Model):
    title_name = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
       return self.title_name
