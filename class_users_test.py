import unittest

from class_users import User, Admin


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user_1 = User('Vlad', 'Petrov', 20, 0)

    def test_greet_users(self):
        self.assertEqual(self.user_1.greet_users(), 'Hello Vlad')

    def test_increment_login_attemps(self):
        self.assertEqual(self.user_1.increment_login_attemps(), 1)


if __name__ == '__main__':
    unittest.main()
