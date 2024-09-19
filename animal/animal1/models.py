from django.db import models


class Animal(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    type = models.ForeignKey('TypeAnimal', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class TypeAnimal(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
