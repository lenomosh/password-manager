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
        self.username = None
        self.password = None
        self.token = None

    def new_user(self, username, password):
        """
        Created a new user
        :param username:
        :param password:
        :return:
        """
        self.username = username
        self.password = password
        self.token = self.generate_token
        print(f"Welcome {username}, An account has been created for you, you can use the following token for "
              f"authentication.\n Your access token is {self.token} ")
        return {'username': username, 'password': password}

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
                    password = str(acc[0]['password'])
                    cb.copy(password)
                    print("Password has been copied to clipboard.")
                    return acc[0]
                except IndexError:
                    print('Account not found')
                    return 'Account not found'
        else:
            print('You have no account yet.')

    def login(self,username,password):
        """
        Prompt user for username and password.
        It then authenticates the user and generates an access_token

        :return: string
        """
        if username == self.username and password == self.password:
            self.token = self.generate_token
            return f"Welcome back {username}, you access token is {self.token}"
        else:
            return "Incorrect Username or password. Please try again"

    def logout(self):
        """
        Logout out the user and clears access token
        :return:
        """
        self.token = None
        print(f"Logout was successful. See you soon {self.username}")

    def view_all_accounts(self):
        """
        Return a dictionary of all accounts that belongs to the user

        :return: self.accounts
        """
        print(f"You have {len(self.accounts)} accounts with us.")
        # for ac in self.accounts:
        #     print(ac)
        return self.accounts
