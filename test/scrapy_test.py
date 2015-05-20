__author__ = 'Administrator'


import unittest

from data.model.models import Job
from libs.lib import user_email_check
from data.model.nosql_data import JobData
from data.model.base import Base,DBSession

class MyTestCase(unittest.TestCase):
    #
    # def test_insert_data(self):
    #     self.assertEqual(True,Job.add_data_from_v2ex(DBSession,
    #                                                  company="qweqwe",
    #                                                  info_link="http://www.v2ex.com",
    #                                                  skill="python"))

    # def test_insert_data_job(self):
    #     self.assertEqual(True,JobData.add_nedu_job_main_key(DBSession,"job_key",["python"]))
    def test_send_email(self):
        from application import mail
        self.assertEqual(True,user_email_check("190810401@qq.com",mail))

if __name__ == '__main__':
    unittest.main()
