from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('título', max_length=200)
    content = models.TextField('conteúdo (HTML)')
    posted_at = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='post'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='autor',
    )
    text = models.TextField('comentário')
    posted_at = models.DateTimeField('data de postagem', default=timezone.now)

    class Meta:
        ordering = ['-posted_at']

    def __str__(self):
        return f'Comentário de {self.author} em {self.post}'
