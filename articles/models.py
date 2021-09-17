from django.db import models

# Create your models here.

class Article(models.Model): # inherits from models

    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank = True)
    # author = models.CharField(max_length=30)

    # Everytime you add to a model:
    #   python manage.py makemigrations
    #   python manage.py migrate

    def snippet(self):
        continueingString = '...' if len(self.body) > 50 else ''
        return self.body[:50] + continueingString

    def __str__(self): # Samme som toString()
        return self.title

    
