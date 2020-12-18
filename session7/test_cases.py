import os
import unittest
import json
from flaskr import create_app
from models import Account, setup_db


class AccountTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bank_testing"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'username', 'password', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_account = {
            'first_name': "Omar",
            'last_name': "Gaber",
            'balance': 5000
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    # def test_index(self):
    #     res = self.client().get('/')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['message'], "Hello Udacians")

    # def test_get_user_accounts(self):
    #     """Test  """
    #     res = self.client().get('/accounts')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertEqual(data['total_accounts'], 10)

    # def test_404_access_undefined_route(self):
    #     res = self.client().get('/bateekh')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Resource Not Found')

    def test_create_account(self):
        res = self.client().post('/accounts/create',
                                 json=self.new_account)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['first_name'], self.new_account['first_name'])
        self.assertEqual(data['last_name'], self.new_account['last_name'])
        # self.assertEqual(account.format())

    # def test_getting_name_counts(self):
    #     res = self.client().post('/accounts/create',
    #                              json={"search": "Omar"})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['total_records'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
