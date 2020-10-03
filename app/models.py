from django.db import models

"""
- Todo
    - Title
    - DateTime
    - Status
"""

class Todo(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)