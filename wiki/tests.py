from django.test import TestCase
from django.contrib.auth.models import User
from . models import NeighborHood


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