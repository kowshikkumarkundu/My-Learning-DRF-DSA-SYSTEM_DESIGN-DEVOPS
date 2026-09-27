from django.db import models

# class Product(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     discount = models.IntegerField()
#     cost_price = models.IntegerField()

#     def __str__(self):
#         return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )
