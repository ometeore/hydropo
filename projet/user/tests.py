from django.test import TestCase, Client
from user.models import MyUser

class TestStatus(TestCase):
    def setUp(self):
        
        self.user = MyUser.objects.create_user(username='jacob', email='jacob@…', password='top_secret')

    def test_home(self):
        ### Test qu'on a bien une reponse en demandant l'accueil ###
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_connect_user(self):
        ### Test la connection d'un utilisateur ###
        response = self.client.post('/user/', {'identifiant': 'jacob', 'password': 'top_secret'})
        self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)


    def test_disconect_user(self):
        ### test qu'au click sur disconect le user est logout ###
        pass

    def test_create_user(self):
        ### test le resultat de la création d'un utilisateur ###
        dict_to_post = {
                            'last_name': 'bob',
                            'first_name': 'dOckland',
                            'Username':'bob',
                            'email':'bob@oak.land',
                            'confirm_password':'password',
                            'password': 'password'
                        }
        response = self.client.post('/user/create', dict_to_post)



    def test_search(self):
        #### Test le resultat d'une recherche depuis / d'un aliment 
        #### l'input est sur '/' le post pointe vers '/aliment/recherche'
        ####la recherche est un name contains
        pass