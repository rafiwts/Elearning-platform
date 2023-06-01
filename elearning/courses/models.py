from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Subject(models.Model):
    title: str = models.CharField(max_length=200)
    slug: str = models.SlugField(max_length=200,
                                 unique=True)
    
    class Meta:
        ordering = ('title',)
    
    def __str__(self) -> str:
        return self.title
    

class Course(models.Model):
    owner: int = models.ForeignKey(User,
                                   related_name='courses_created',
                                   on_delete=models.CASCADE)
    subject: int = models.ForeignKey(Subject,
                                     related_name='courses',
                                     on_delete=models.CASCADE)
    title: str = models.CharField(max_length=200)
    slug: str = models.SlugField(max_length=200,
                                 unique=True)
    overview: str = models.TextField()
    created: int = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return self.title


class Module(models.Model):
    course: int = models.ForeignKey(Course,
                                    null=True,
                                    related_name='modules',
                                    on_delete=models.SET_NULL)
    title: str = models.CharField(max_length=200)
    description: str = models.TextField(blank=True)


class Content(models.Model):
    module: int = models.ForeignKey(Module,
                                    related_name='contents',
                                    on_delete=models.CASCADE)
    content_type: int = models.ForeignKey(ContentType,
                                          on_delete=models.CASCADE)
    object_id: int = models.PositiveBigIntegerField()
    item: int = GenericForeignKey('content_type', 'object_id')


class ItemBase(models.Model):
    owner: int = models.ForeignKey(User,
                                   related_name='%(class)s_related', # name depending on a model
                                   on_delete=models.CASCADE)
    title: str = models.CharField(max_length=250)
    created: int = models.DateField(auto_now_add=True)
    updated: int = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
    

class Text(ItemBase):
    content: str = models.TextField()


class File(ItemBase):
    file: str = models.FileField(upload_to='files')


class Image(ItemBase):
    file: str = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()