from django.test import TestCase
from django.contrib.auth.models import User
from . models import NeighborHood, Business


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

        