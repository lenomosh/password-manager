from unittest import TestCase, main
from User import User


class TestUser(TestCase):
    u = User()

    def test_user_new_user(self):
        self.assertEqual(self.u.new_user('john', 'keba'), {'username': 'john', 'password': 'keba'})

    def test_generate_password(self):
        self.assertEqual(len(self.u.generate_password()), 8)
        self.assertEqual(len(self.u.generate_password(20)), 20)

    def test_add_account(self):
        self.assertDictEqual(self.u.add_account('ig', 'if', 'qwertyuio'),
                             {'account_name': 'ig', 'username': 'if', 'password': 'qwertyuio'})

    def test_get_account_details(self):
        # Uncomment next Line if you want to run only this text block
        # self.assertEqual(self.u.get_account_details('retrytfyt'), 'You have no account yet.')
        self.u.add_account('facebook', 'facebook_user', 'facebook_pass')
        self.assertDictEqual(self.u.get_account_details('facebook'),
                             {'account_name': 'facebook', 'username': 'facebook_user', 'password': 'facebook_pass'})
        self.assertEqual(self.u.get_account_details('wefeuuei'), 'Account not found')


if __name__ == '__main__':
    main()
