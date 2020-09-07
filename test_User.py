from unittest import TestCase, main
from User import User


class TestUser(TestCase):
    u = User()

    def test_user_new_user(self):
        self.assertEquals(self.u.new_user('john', 'keba'), {'username': 'john', 'password': 'keba'})

    def test_generate_password(self):
        print(self.u.generate_password(20))
        self.assertEqual(len(self.u.generate_password()), 8)
        self.assertEqual(len(self.u.generate_password(20)), 20)


if __name__ == '__main__':
    main()
