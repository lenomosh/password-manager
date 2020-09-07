from Credentials import Credentials
from getpass import getpass
import pyperclip as cb


class User(Credentials):
    """
    The class is responsible for creating, user account, logging in, logging out
    and managing accounts for different accounts
    """
    def __init__(self):
        super().__init__()
        self.username = 'leno'
        self.password = 'leno'
        self.token = 'jkakj'
        if not self.token:
            print('You need to either login or sign Up to continue')
            user_input = int(input("Reply with 1 to login and 2 to sign Up (1/2): "))
            if user_input == 1:
                self.login()
            else:
                self.new_user()

    def new_user(self, username=None, password=None):
        """
        Created a new user
        :param username:
        :param password:
        :return:
        """
        if username is None and password is None:
            username = input("Username: ")
            password = getpass("Password: ")
        self.username = username
        self.password = password
        self.token = self.generate_token
        print( f"Welcome {username}, An account has been created for you, you can use the following token for " \
               f"authentication. Your access token is {self.token} ")
        return {'username':username,'password':password}

    def get_account_details(self, account_name):
        """
        return account details for the specified account name
        :param account_name:
        :return:
        """
        if len(self.accounts) != 0:

            if (acc['account_name'] == account_name for acc in self.accounts):
                try:
                    acc = list((acc for acc in self.accounts if acc['account_name'] == account_name))
                    print(acc)
                    password = str(acc[0]['password'])
                    cb.copy(password)
                    print(acc[0]['password'])
                    print("Password has been copied to clipboard.")
                    return acc[0]
                except IndexError:
                    return 'Account not found'
            return 'Account  not found'
        else:
            return 'You have no account yet.'

    def login(self):
        username = input("Username: ")
        password = getpass("Password: ")
        if username == self.username and password == self.password:
            self.token = self.generate_token
            return f"Welcome back {username}, you access token is {self.token}"
        else:
            return "Incorrect Username or password. Please try again"

    def logout(self):
        self.token = None
        return f"Logout was successful. See you soon {self.username}"

    def view_all_accounts(self):
        print(f"You have {len(self.accounts)} accounts with us.")
        for ac in self.accounts:
            print(ac)
