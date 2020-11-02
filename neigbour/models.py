from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class neighbourhood(models.Model):
    Name = models.CharField(max_length = 60)
    City = models.CharField(max_length = 30)
    Town = models.CharField(max_length = 60)
    Info = models.TextField(max_length=500)
    Occupantscount = models.IntegerField()

    def savehood(self):
        self.save()

    def deletehood(self):
        self.delete()

    def search(cls, searchterm):
        searchresults = cls.objects.filter(Name = searchterm)
        return searchresults

class user(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    Profilephoto = models.ImageField(upload_to= 'users/')
    Email = models.CharField(max_length = 30)
    Phone = models.IntegerField()
    Neighbourhood =models.ForeignKey(neighbourhood, on_delete = models.CASCADE)

    def saveuser(self):
        self.save()

    def deleteuser(self):
        self.delete()

    def update(self, profile):
        profile.save()


class Business(models.Model):
    Name = models.CharField(max_length = 30)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.CharField(max_length = 60)
    Description = models.CharField(max_length = 30)
    Neighbourhood = models.ForeignKey(neighbourhood, on_delete =  models.CASCADE)
    Email = models.CharField(max_length= 30)
    Phone = models.IntegerField()

    def savebusiness(self):
        self.save()

    def deletebusiness(self):
        self.delete()

    @classmethod
    def searchbusiness(cls, category):
        searchresults = cls.objects.filter(category = category)
        return searchresults

    




