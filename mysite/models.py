from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return self.first_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title


#Assignment [ 2 ]
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    #course = models.ManyToManyField('Course')

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    office = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.EmailField()

class Course(models.Model):
    name = models.CharField(max_length=30)
    classroom = models.CharField(max_length=50)
    code = models.CharField(max_length=60)
    time = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)