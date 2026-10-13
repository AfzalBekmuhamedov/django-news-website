from tkinter.constants import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import AUTH_USER_MODEL


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Article(models.Model):
    title = models.CharField(max_length=250)
    info = models.TextField()
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def get_image(self):
        try:
            return self.image.url
        except:
            return "https://png.pngtree.com/png-vector/20221125/ourlarge/pngtree-no-image-available-icon-flatvector-illustration-pic-design-profile-vector-png-image_40966566.jpg"

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.TextField()
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title