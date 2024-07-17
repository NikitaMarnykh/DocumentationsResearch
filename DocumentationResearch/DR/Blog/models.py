from django.db import models


# Модель постов
class Post(models.Model):
    created = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    title: str = models.CharField(null=False, max_length=100, blank=True, default='')
    body: str = models.TextField(null=False, blank=True, default='', max_length=30000)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title, self.body, self.owner, self.created


# Модель комментариев
class Comment(models.Model):
    created = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    body: str = models.TextField(null=False, blank=True, default='', max_length=2000)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.owner

    def __repr__(self):
        return self.body, self.owner, self.post, self.created


# Модель категорий
class Category(models.Model):
    name: str = models.CharField(max_length=100, blank=False, null=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name, self.owner, self.posts
