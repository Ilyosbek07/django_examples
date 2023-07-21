from ckeditor.fields import RichTextField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(BaseModel):
    username = models.CharField(max_length=55)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Occupation(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'occupation'
        verbose_name_plural = 'occupations'


class AuthorSocialMedia(BaseModel):
    name = models.CharField(max_length=55)
    icon = models.FileField()
    url = models.URLField()

    def __str__(self):
        return self.name


class Author(BaseModel):
    name = models.CharField(max_length=55)
    address = models.TextField()
    social_media = models.ForeignKey(
        AuthorSocialMedia,
        related_name='author_social',
        on_delete=models.CASCADE
    )
    occupation = models.ForeignKey(
        Occupation,
        related_name='author_occupation',
        on_delete=models.CASCADE
    )
    picture = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    subscription_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'subscription'


class InstagramLink(BaseModel):
    picture = models.ImageField()
    url = models.URLField()

    class Meta:
        verbose_name = 'InstagramLink'


class Category(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'


class Tag(BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'


class Comment(BaseModel):
    user = models.ManyToManyField(
        User,
        related_name='comment',
    )
    text = models.TextField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'comment'


class Article(BaseModel):
    name = models.CharField(max_length=125)
    author = models.ForeignKey(
        Author,
        related_name='article',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='tag',
    )
    description = RichTextField(config_name='awesome_ckeditor')
    read_time = models.IntegerField()
    comment = models.ForeignKey(
        Comment,
        related_name='comment',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'


class FAQ(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FAQ'


class Contact(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
