from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    price=models.DecimalField(decimal_places=3,max_digits=9)
    published_year=models.IntegerField()
    isbn=models.CharField(max_length=80)
        
    