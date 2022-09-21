from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(null=True, upload_to='uploads/%Y/%m')

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name


class MyModelBase(models.Model):
    subject = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        abstract = True


class Course(MyModelBase):
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ["-id"]

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)

class Lesson(MyModelBase):
    class Meta:
        unique_together = ('subject', 'course')

    content = models.TextField()
    course = models.ForeignKey(Course,
                               related_name="lesson",
                               on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag', related_name="lesson",
                                  blank=True, null=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class ActionBase(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Action(ActionBase):
    LIKE, HAHA, HEART = range(3)
    ACTIONS = [
        (LIKE, 'like'),
        (HAHA, 'haha'),
        (HEART, 'heart')
    ]
    type = models.PositiveSmallIntegerField(choices=ACTIONS, default=LIKE)


class Comment(models.Model):
    content = models.TextField(max_length=255)
    lesson = models.ForeignKey(Lesson, related_name='comments',
                               on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


class Rating(ActionBase):
    rate = models.SmallIntegerField(default=0)

