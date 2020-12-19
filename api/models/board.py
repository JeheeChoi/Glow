from django.db import models
from django.contrib.auth import get_user_model

# Board model
class Board(models.Model):

  title = models.CharField(max_length=50)
  topic = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"Board: {self.title} - {self.topic} is available. Check it out!"

  def as_dict(self):
    """Returns dictionary version of Board models"""
    return {
        'id': self.id,
        'title': self.title,
        'topic': self.topic,
    }
