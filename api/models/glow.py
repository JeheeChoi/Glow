from django.db import models
from django.contrib.auth import get_user_model

# Glow model
class Glow(models.Model):

  message = models.TextField()
  # Not sure how to add firstName/lastName to author
  name = models.CharField(max_length=100)
  board_id = models.ForeignKey('Board', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    return f"Glow Message: '{self.message}' by {self.name}."

  def as_dict(self):
    return {
        'id': self.id,
        'message': self.message,
        'written by': self.name,
        'board_id': self.board_id,
    }
