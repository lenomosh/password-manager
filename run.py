from User import User
from threading import Thread
from getpass import getpass
from pyfiglet import Figlet
from terminaltables import AsciiTable

f = Figlet(font='banner3')


class RunApp:

    def __init__(self, ):
        print(f.renderText("Welcome to Password Manager"))
        self.user = User()

    def sign_up(self):
        print(f.renderText("SignUp"))
        if not self.user.token:
            print('You need to either login or sign Up to continue')
            user_input = int(input("Reply with 1 to login and 2 to sign Up (1/2): "))
            username = input('Username: ')
            if user_input == 1:
                password = getpass('Password: ')
                response = self.user.login(username, password)
                print(response)
            else:
                print("1. Generate a password")
                print("2. Enter your own password")
                user_input = int(input("Your Response (1/2): "))
                if user_input == 1:
                    password = self.user.generate_password()
                else:
                    password = input('Enter new password: ')

                self.user.new_user(username, password)

    def create_credentials_account(self):
        print(f.renderText("Create new credential account"))
        account = input('Account Name: ')
        username = input('Account Username: ')
        print("1. Generate a password")
        print("2. Enter your own password")
        user_input = int(input("Your Response (1/2): "))
        if user_input == 1:
            password = self.user.generate_password()
        else:
            password = input('Enter new password: ')
        if self.user.add_account(account, username, password):
            print("Account Created Successfully")

    def login(self):
        username = input("Username: ")
        password = getpass("password: ")
        print(self.user.login(username, password))

    def delete_credentials_account(self):
        account_name = input("Account Name: ")
        self.user.delete_account(account_name)

    def view_credential_account(self):
        account_name = input('Account Name: ')
        account = self.user.get_account_details(account_name)
        datatable = [
            ["Account Name", "Account Username", "Account Password"]
        ]
        if account:
            datatable.append(account.values())

        table = AsciiTable(datatable)
        print(table.table)

    def view_all_accounts(self):
        accounts = self.user.view_all_accounts()
        datatable = [
            ["Account Name", "Account Username", "Account Password"]
        ]
        if accounts:
            for account in accounts:
                datatable.append(account.values())

        table = AsciiTable(datatable)
        print(table.table)

    def dashboard(self):
        while True:
            if self.user.token:
                print("1. Add Account\n"
                      "2. View Specific Account\n"
                      "3. View All Accounts\n"
                      "4. Delete Account\n"
                      "5. Logout")

                user_input = input('Your response: ')
                if user_input == '1':
                    self.create_credentials_account()
                elif user_input == '2':
                    self.view_credential_account()
                elif user_input == '3':
                    self.view_all_accounts()
                elif user_input == '4':
                    self.delete_credentials_account()
                elif user_input == '5':
                    self.user.logout()
                    pass
            else:
                print("1. Login\n"
                      "2. Quit")
                response = input("Your Response: ")
                if response == '1':
                    self.login()
                elif response == '2':
                    print("Goodbye, see you soon")
                    pass
                pass
            pass

    def run(self):
        if __name__ == '__main__':
            Thread(target=self.sign_up()).start()
            Thread(target=self.create_credentials_account()).start()
            if self.user.token:
                Thread(target=self.dashboard()).start()


if __name__ == '__main__':
    RunApp().run()
