from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # models.SETNULL
    def __str__(self):
        return self.title

