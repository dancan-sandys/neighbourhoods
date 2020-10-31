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




