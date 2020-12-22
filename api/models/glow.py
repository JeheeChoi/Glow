from django.db import models
from django.contrib.auth import get_user_model

# Glow model
class Glow(models.Model):

  message = models.TextField()
  # Not sure how to add firstName/lastName to author
  author = models.ForeignKey('User', related_name='glows', on_delete=models.CASCADE)
  board_id = models.ForeignKey('Board', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"Glow Message: '{self.message}' by {self.author}."

  def as_dict(self):
    return {
        'id': self.id,
        'message': self.message,
        'author': self.author,
        'board': self.board_id
    }
