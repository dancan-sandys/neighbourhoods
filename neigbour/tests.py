from django.test import TestCase
from .models import user, Business, neighbourhood
from django.contrib.auth.models import User

# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
       
        self.new_neighbourhood = neighbourhood(Name='Kasarani', City='Nairobi', Town='Kasarani',Info='Yes', securitycontact='955', healthcontact='955', Occupantscount='3')
        self.new_User = User(username= 'sandys', password='Stanford2020*')
        self.new_user = user(user= self.new_User,Neighbourhood= self.new_neighbourhood)

    def tearDown(self):
        user.objects.all().delete()
        neighbourhood.objects.all().delete()
        Business.objects.all().delete()


    def testinstance(self):

        self.assertTrue(isinstance(self.new_user, user))
    def testsaveuser(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_user.saveuser()
        users = user.objects.all()
        self.assertTrue(len(users)>0)

    def testdeleteuser(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_user.saveuser()
        users = user.objects.all()
        self.assertTrue(len(users)>0)
        self.new_user.deleteuser()
        users = user.objects.all()
        self.assertEqual(len(users),0)



class TestNeighbourhood(TestCase):
    def setUp(self):
       
        self.new_neighbourhood = neighbourhood(Name='Kasarani', City='Nairobi', Town='Kasarani',Info='Yes', securitycontact='955', healthcontact='955', Occupantscount='3')
        self.new_User = User(username= 'sandys', password='Stanford2020*')
        self.new_user = user(user= self.new_User,Neighbourhood= self.new_neighbourhood)

    def tearDown(self):
        user.objects.all().delete()
        neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def testinstance(self):

        self.assertTrue(isinstance(self.new_neighbourhood, neighbourhood))
    def testsaveneighbourhood(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_user.saveuser()
        neighbourhoods = neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)

    def testdeleteneighbourhood(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_user.saveuser()
        neighbourhoods = neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)>0)
        self.new_neighbourhood.deletehood()
        neighbourhoods = neighbourhood.objects.all()
        self.assertEqual(len(neighbourhoods),0)




class TestNeighbourhood(TestCase):
    def setUp(self):
       
        self.new_neighbourhood = neighbourhood(Name='Kasarani', City='Nairobi', Town='Kasarani',Info='Yes', securitycontact='955', healthcontact='955', Occupantscount='3')
        self.new_User = User(username= 'sandys', password='Stanford2020*')
        self.new_business = Business(owner= self.new_User,Neighbourhood= self.new_neighbourhood)

    def tearDown(self):
        Business.objects.all().delete()
        neighbourhood.objects.all().delete()
        Business.objects.all().delete()

    def testinstance(self):

        self.assertTrue(isinstance(self.new_neighbourhood, neighbourhood))
    def testsaveuser(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_business.savebusiness()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses)>0)

    def testdeleteuser(self):
        self.new_User.save()
        self.new_neighbourhood.save()
        self.new_business.savebusiness()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses)>0)
        self.new_business.deletebusiness()
        businesses = Business.objects.all()
        self.assertEqual(len(businesses),0)
