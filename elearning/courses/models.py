from django.db import models
from django.contrib.auth.models import User


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