from django.db import models

from django.utils.timezone import now
from mdeditor.fields import MDTextField

# from core.accouts.models import BlogUser


# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField('create time', default=now)
    last_mod_time = models.DateTimeField('last modified time', default=now)

    def save(self, *args, **kwargs):
        super().save()

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField('category name', max_length=30, unique=True)
    index = models.IntegerField('order by larger num', default=0)

    def __str__(self):
        return self.name


class Article(BaseModel):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'publish')
    )
    title = models.CharField('title', max_length=200, unique=True)
    body = MDTextField('article content')
    pub_time = models.DateTimeField('publish time', default=now)
    status = models.CharField(
        'article status',
        max_length=1,
        choices=STATUS_CHOICES,
        default='d'
    )
    # author = models.ForeignKey(BlogUser,
    #                            verbose_name='author',
    #                            null=True, blank=True,
    #                            on_delete=models.CASCADE)
    article_order = models.IntegerField('order by larger num', blank=False, null=False, default=0)
    category = models.ForeignKey(Category,
                                 verbose_name='category',
                                 blank=False, null=False,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
