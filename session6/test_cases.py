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
            'santarabantoosoo', 123, 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_account = {
            'first_name': "Omar",
            'last_name': "Gaber",
            'balance': 5000
        }

    def tearDown(self):
        """Executed after each test"""
        pass

    # TODO add tests for endpoints and errors.  


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()



