from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserModel(models.Model, BaseModel):
    username = models.CharField(max_length=55)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class OccupationModel(models.Model, BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'occupation'
        verbose_name_plural = 'occupations'


class AuthorSocialMedia(models.Model, BaseModel):
    name = models.CharField(max_length=55)
    icon = models.FileField()
    url = models.URLField()

    def __str__(self):
        return self.name


class AuthorModel(models.Model, BaseModel):
    name = models.CharField(max_length=55)
    address = models.TextField()
    social_media = models.ForeignKey(
        AuthorSocialMedia,
        related_name='author_social',
        on_delete=models.CASCADE
    )
    occupation = models.ForeignKey(
        OccupationModel,
        related_name='author_occupation',
        on_delete=models.CASCADE
    )
    picture = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'


class SubscriptionModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.CASCADE
    )
    subscription_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'subscription'


class InstagramLinkModel(models.Model, BaseModel):
    picture = models.ImageField()
    url = models.URLField()

    class Meta:
        verbose_name = 'InstagramLink'


class CategoryModel(models.Model, BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'


class TagModel(models.Model, BaseModel):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'


class CommentModel(models.Model, BaseModel):
    user = models.ManyToManyRel(
        UserModel,
        related_name='comment',
    )
    text = models.TextField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'comment'


class ArticleModel(models.Model, BaseModel):
    name = models.CharField(max_length=125)
    author = models.ForeignKey(
        AuthorModel,
        related_name='article',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        CategoryModel,
        related_name='category',
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyRel(
        TagModel,
        related_name='tag',
    )
    description = 111
    read_time = models.IntegerField()
    comment = models.ForeignKey(
        CommentModel,
        related_name='comment',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'


class FAQModel(models.Model, BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FAQ'


class ContactModel(models.Model, BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
