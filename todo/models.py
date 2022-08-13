from django.db import models

# Create your models here.
class toDo(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=144)
    
    WORK = "WORK"
    PERSONAL = "PERSONAL"
    CAT_CHOICES = [
        (WORK, 'WORK'),
        (PERSONAL, 'PERSONAL')
    ]
    category_type = models.CharField(max_length=24, choices=CAT_CHOICES, default=PERSONAL)

    def __str__(self):
        return self.title