from django.test import TestCase
from django.contrib.auth.models import User
from . models import NeighborHood, Business, Profile


class NeighborhoodTestClass(TestCase):
    '''
    Test class to test the behaviour of the Neighborhood class and methods
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        # Creating a new user
        self.new_user = User(username = 'Doe', email = 'johndoe@company.com', password = 'test_pass')
        self.new_user.save()

        # Creating a new neighborhood
        self.new_neighborhood = NeighborHood(id = 1, name = 'test neighborhood', location = 'test location', occupants = 10, admin = self.new_user)
        self.new_neighborhood.save()

    def test_instance(self):
        '''
        Method to test if the new_neighborhood object is an instance of the Neighborhood model
        '''

        self.assertTrue(self.new_neighborhood, NeighborHood)

    def test_delete(self):
        '''
        Method to test the delete neighborhood method
        '''
        
        NeighborHood.delete_neighborhood(self.new_neighborhood.id)
        neighborhoods = NeighborHood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)

    def test_find_neighborhood(self):
        '''
        Method to test the find neighborhood method
        '''

        neighborhood = NeighborHood.find_neigborhood(1)
        self.assertEqual(neighborhood.name, 'test neighborhood')

class BusinessTestClass(TestCase):
    '''
     Test class to test the behaviour of the Business class and methods
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        # Creating a new user
        self.new_user = User(username = 'Doe', email = 'johndoe@company.com', password = 'test_pass')
        self.new_user.save()

        # Creating a new neighborhood
        self.new_neighborhood = NeighborHood(id = 1, name = 'test neighborhood', location = 'test location', occupants = 10, admin = self.new_user)
        self.new_neighborhood.save()

        # Creating a new business
        self.new_business = Business(id = 1, name = 'test business', description = 'test business description', email = 'info@business.com', user = self.new_user, neighborhood = self.new_neighborhood)
        self.new_business.save()

    def test_instance(self):
        '''
        Method to test if the new_business object is an instance of the Business model class
        '''

        self.assertTrue(self.new_business, Business)

    def test_delete(self):
        '''
        Method to test the delete business method
        '''
        
        Business.delete_business(self.new_business.id)
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)

    def test_find_business(self):
        '''
        Method to test the find business method
        '''

        business = Business.find_business(1)
        self.assertEqual(business.name, 'test business')

class ProfileTestClass(TestCase):
    '''
     Test class to test the behaviour of the Profile class and methods
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        # Creating a new user
        self.new_user = User(username = 'Doe', email = 'johndoe@company.com', password = 'test_pass')
        self.new_user.save()

        # Creating a new neighborhood
        self.new_neighborhood = NeighborHood(id = 1, name = 'test neighborhood', location = 'test location', occupants = 10, admin = self.new_user)
        self.new_neighborhood.save()

        # Creating a new profile
        self.new_profile = Profile(id = 1, name = 'test profile', bio = 'test profile bio', location = 'test location', user = self.new_user, neighborhood = self.new_neighborhood)
        self.new_profile.save()

    def test_instance(self):
        '''
        Method to test if the new_profile object is an instance of the Profile model class
        '''

        self.assertTrue(self.new_profile, Profile)

    def test_delete(self):
        '''
        Method to test the delete profile method
        '''
        
        Profile.delete_profile(self.new_profile.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    def test_find_profile(self):
        '''
        Method to test the find profile method
        '''

        profile = Profile.find_profile(1)
        self.assertEqual(profile.name, 'test profile')