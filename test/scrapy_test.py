__author__ = 'Administrator'


import unittest
import os
from application import app
import tempfile


from data.model.models import Job
from libs.lib import user_email_check
from data.model.nosql_data import JobData
from data.model.base import Base,DBSession

from libs.lib import user_email_check

class NeduJob(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        cls.app = app.test_client()
        app.init_db()

    @classmethod
    def tearDownClass(cls):
        os.close(cls.db_fd)
        os.unlink(app.config["DATABASE"])


    def test_check_email(self):
        self.assertTrue(user_email_check("190810401@qq.com"))


if __name__ == '__main__':
    unittest.main()
