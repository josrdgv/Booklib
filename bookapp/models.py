from django.db import models

# Create your models here.



# class author is a another table ,this is going to connect to book table using foreign key
class Author(models.Model):
    author_name=models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.author_name)


class Book(models.Model):
    title=models.CharField(max_length=200,null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media')
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    quantity=models.IntegerField()

    def __str__(self):
        return "{}".format(self.title)