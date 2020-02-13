from django.test import TestCase
from django.urls import reverse


# Create your tests here.
from faker import Faker


class TestContact(TestCase):

    def test_contact_is_valid(self):
        data = {
            'email': 'yadritig+5@gmail.com',
            'subject': 'subject',
            'text': 'text',
        }

        response = self.client.post(reverse('contact'), data)
        assert response.status_code == 302

        data['email'] = 'WRONG'
        response = self.client.post(reverse('contact'), data)
        assert response.status_code == 200


class TestStudents(TestCase):
    fake = Faker()
    # fixtures = ['db.json']

    # def setUp(self) -> None:
    #     print('Setup')
    #
    # def tearDown(self) -> None:
    #     print('tearDown')
    #
    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')
    #     call_command('loaddata', 'db.json', verbosity=0)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')

    def _gen_data(self):
        return {
            'subject': self.fake.word(),
            'text': self.fake.text(),
        }

    def test_contact_form(self):
        data = {
            'email': self.fake.email(),
            **self._gen_data(),
        }
        # data.update(self._gen_data())

        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 302
        print()

    def test_contact_form_wrong_email(self):
        data = {
            'email': 'wrong_email',
            'subject': self.fake.word(),
            'text': self.fake.text(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200

    def test_contact_form_empty_subject(self):
        data = {
            'email': self.fake.email(),
            'subject': '',
            'text': self.fake.text(),
        }
        response = self.client.post(reverse('contact'), data=data)
        assert response.status_code == 200
