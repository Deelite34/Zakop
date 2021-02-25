from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Finding(models.Model):
    finding_id = models.AutoField(primary_key=True)
    finding_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.SET('Deleted'))
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    permalink = models.CharField(max_length=300)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "findings"

    def __str__(self):
        return f'ID:{self.finding_id} \"{self.title}\"'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "tags"


class FindingRating(models.Model):
    finding_id = models.ForeignKey('Finding', on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "finding_ratings"


class ZakopUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=30)
    icon_file_name = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=75)

    class Meta:
        verbose_name_plural = "users"

    def __str__(self):
        return f'ID:{self.user_id} \"{self.name}\"'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    finding_id = models.ForeignKey('Finding', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    attachment = models.CharField(max_length=300)
    parent_comment_id = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "comments"


class CommentsRating(models.Model):
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE)
    vote = models.IntegerField()
    user = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "comments_ratings"
