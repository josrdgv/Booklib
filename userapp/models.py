from django.contrib.auth.models import User
from django.db import models
from bookapp.models import Book,Author


# Create your models here.


# class author is a another table ,this is going to connect to book table using foreign key
# class Author(models.Model):
#     author_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return "{}".format(self.author_name)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=200, null=True)
#     price = models.IntegerField(null=True)
#     image = models.ImageField(upload_to='book_media')
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "{}".format(self.title)


class Cart(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)

class cartitem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


from django.db import models

# Create your models here.
