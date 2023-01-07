from django.db import models

# Create your models here.
class Topic(models.Model):
    """Topic knowed by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Returns the representations of the model as a text string"""
        return self.text