from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/%Y/%m/%d")
    urr = models.CharField(max_length=200, blank=True)

    def __str__(self):
         return self.title


    class Meta:
        verbose_name = "Surat"
        verbose_name_plural = "Suratlar"


class About(models.Model):
    title = models.CharField(max_length=222, blank=True)
    desc = models.CharField(max_length=222, blank=True)
    name = models.CharField(max_length=222, blank=True)
    degree = models.CharField(max_length=222, blank=True)
    phone = models.CharField(max_length=222, blank=True)
    address = models.CharField(max_length=222, blank=True)
    birthday = models.CharField(max_length=222, blank=True)
    experience = models.CharField(max_length=222, blank=True)
    email = models.CharField(max_length=222, blank=True)
    freelance = models.CharField(max_length=222, blank=True)
    image = models.ImageField(upload_to="about/%Y/%m/%d")



    def __str__(self):
         return self.title


class Edication(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title
    
class Exper(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()


    def __str__(self) -> str:
        return self.title
    

class Cantact(models.Model):
    y_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self) -> str:
        return self.email
    