from django.db import models


class Tag(models.Model):

    name = models.SlugField(max_length=25, db_index=True, 
        unique=True, help_text='Тег')

    def __str__(self):
        return self.name


class Post(models.Model):

    created = models.DateTimeField(auto_now_add=True, 
        help_text='Дата создания поста')
    read = models.CharField(max_length=2, default='1', 
        null=True, blank=True, help_text='Время на чтение')
    title = models.CharField(max_length=200, help_text='Заголовок поста')
    slug = models.SlugField(help_text='Слаг поста', db_index=True,
        unique=True, null=True, blank=True)
    content = models.TextField(help_text='Содержание поста')
    image = models.FileField(upload_to='images/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, help_text='Теги')

    def __str__(self):
        return self.title
