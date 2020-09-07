from unittest import TestCase, main
from User import User


class TestUser(TestCase):
    u = User()
    def test_user_new_user(self):
        self.assertEquals(u.new_user('john', 'keba'),{'username':'john','password':'keba'})
    def test_account_details(self):

if __name__ == '__main__':
    main()