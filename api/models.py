from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class LibUser(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RentBook(models.Model):
    book = models.ForeignKey(Book , on_delete=models.CASCADE)
    user = models.ForeignKey(LibUser , on_delete=models.CASCADE)
    rentDate = models.DateTimeField(auto_now_add=True)
    reterneddate = models.DateTimeField(null=True , blank= True)

    def __str__(self):
        return self.rentDate    


class BookCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name    

