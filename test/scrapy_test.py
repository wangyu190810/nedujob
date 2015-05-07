__author__ = 'Administrator'


import unittest

from data.model.models import Job
from data.model.base import Base,DBSession

class MyTestCase(unittest.TestCase):

    def test_insert_data(self):
        self.assertEqual(True,Job.add_data_from_v2ex(DBSession,
                                                     company="qweqwe",
                                                     info_link="http://www.v2ex.com",
                                                     skill="python"))


if __name__ == '__main__':
    unittest.main()
