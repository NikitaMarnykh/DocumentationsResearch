from django.db import models


# Модель списка задач
class TaskList(models.Model):
    title: str = models.CharField(max_length=50, null=False, blank=False)
    content: str = models.CharField(max_length=5000, null=True, blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title, self.content, self.owner
