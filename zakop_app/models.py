from django.db import models

# Create your models here.


class finding(models.Model):
    finding_id = models.AutoField(primary_key=True)
    finding_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey('user', on_delete=models.SET('Deleted'))
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    permalink = models.CharField(max_length=300)
    tag_id = models.ForeignKey('tag', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "findings"


class tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "tags"


class findings_rating(models.Model):
    finding_id = models.ForeignKey('finding', on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "finding_ratings"


class user(models.Model):
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


class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    finding_id = models.ForeignKey('finding', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    attachment = models.CharField(max_length=300)
    parent_comment_id = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "comments"


class comments_rating(models.Model):
    comment_id = models.ForeignKey('comment', on_delete=models.CASCADE)
    vote = models.IntegerField()
    user = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "comments_ratings"
