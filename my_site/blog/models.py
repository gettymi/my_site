from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email_address = models.EmailField( max_length=254)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Tag(models.Model):
    caption = models.CharField(max_length = 30)

    def __str__(self) -> str:
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length = 50)
    excerpt = models.CharField(max_length = 50)
    image_name = models.CharField(max_length = 50)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique = True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete = models.SET_NULL,null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title
