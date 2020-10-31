from django.db import models

# Create your models here.


class neighbourhood(models.Model):
    Name = models.CharField(max_length = 60)
    City = models.CharField(max_length = 30)
    Town = models.CharField(max_length = 60)
    Occupantscount = models.IntegerField()

    def savehood(self):
        self.save()

    def deletehood(self):
        self.delete()

    def search(cls, searchterm):
        searchresults = cls.objects.filter(Name = searchterm)
        return searchresults

class user(models.Model):
    Name = models.CharField(max_length = 30)
    Profilephoto = models.ImageField()
    Email = models.CharField(max_length = 30)
    Phone = models.IntegerField()
    Neighbourhood =models.ForiegnKey(neighbourhood, on_delete = models.CASCADE)

    def saveuser(self):
        self.save()

    def deleteuser(self):
        self.delete()


class Business(models.Model):
    Name = models.CharField(max_length = 30)
    owner = models.ForiegnKey(user, on_delete = models.CASCADE)
    category = models.CharField(max_length = 60)
    Description = models.CharField(max_length = 30)
    Neighbourhood = models.ForiegnKey(neighbourhood, on_delete =  models.CASCADE)
    Email = models.CharField(max_length= 30)
    Phone = models.IntegerField()

    def savebusiness(self):
        self.save()

    def deletebusiness(self):
        self.delete()

    def searchbusiness(cls, category):
        searchresults = cls.objects.filter(category = category)




