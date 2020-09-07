from Credentials import Credentials
from getpass import getpass
import clipboard as cb


class User(Credentials):
    def __init__(self):
        super().__init__()
        self.username = 'leno'
        self.password = 'leno'
        self.token = 'jkakj'
        if not self.token:
            print('You need to either login or sign Up to continue')
            user_input = int(input("Reply with 1 to login and 2 to sign Up (1/2): "))
            username = input("Username: ")
            password = getpass()
            if user_input == 1:
                self.login(username, password)
            else:
                self.new_user(username, password)

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
        print( f"Welcome {username}, An account has been created for you, you can use the following token for " \
               f"authentication. Your access token is {self.token} ")
        return {'username':username,'password':password}

    def get_account_details(self, account_name):
        """
        return account details for the specified account name
        :param account_name:
        :return:
        """
        if (acc['account_name'] == account_name for acc in self.accounts):
            acc = list((acc for acc in self.accounts if acc['account_name'] == account_name))
            cb.copy(acc[0]['password'])
            print(acc[0]['password'])
            print("Password has been copied to clipboard.")
            return acc[0]
        return 'Account  not found'

    def login(self, username, password):
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
