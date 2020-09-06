from Credentials import Credentials
from getpass import getpass


class User:
    def __init__(self):

        self.username = ''
        self.password = ''
        self.token = None
        self.credentials = Credentials()
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
        self.username = username
        self.password = password
        self.token = Credentials.generate_token
        return f"Welcome {username}, An account has been created for you, you can use the following token for " \
               f"authentication. Your access token is {self.token} "

    def get_account_details(self, account_name):
        if (acc['account_name'] == account_name for acc in self.credentials.accounts):
            return self.credentials.accounts[account_name]
        return 'Account  not found'

    def login(self, username, password):
        if username == self.username and password == self.password:
            self.token = self.credentials.generate_token
            return f"Welcome back {username}, you access token is {self.token}"
        else:
            return "Incorrect Username or password. Please try again"

    def logout(self):
        self.token = None
        return f"Logout was successful. See you soon {self.username}"

    def view_all_accounts(self):
        print(f"You have {len(self.credentials.accounts)} accounts with us.")
        for ac in self.credentials.accounts:
            print(ac)