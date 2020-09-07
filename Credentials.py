from string import ascii_letters, digits, punctuation
from secrets import choice, token_hex


class Credentials:

    def __init__(self):
        self.accounts = []

    def generate_password(self, password_length=None):
        alphabets = ascii_letters + digits + punctuation
        if password_length is None:
            password_length = int(input('Specify the length of password you wish to generate (positive int): '))
        else:
            password_length = int(password_length)
        while True:
            password = ''.join(choice(alphabets) for i in range(password_length))
            try:
                accept = int(
                    input(f"Generated password is {password}.\n Reply with 1 to accept or 2 to generate another "
                          f"password\n"))
                if accept == 1:
                    return password
                else:
                    continue
            except ValueError:
                return f"You've provided an invalid input."

    @property
    def generate_token(self):
        return token_hex(16)

    def add_account(self, account_name, username, password=None):
        if password is None:
            password = self.generate_password()
        account_details = {'account_name': account_name, 'username': username, 'password': password}
        self.accounts.append(account_details)
        return account_details

    def delete_account(self, account_name):
        if any(account['account_name'] == account_name for account in self.accounts):
            user_input = input(f'Do you want to delete your {account_name} account? (y/n): ').lower()
            if user_input == 'y':
                self.accounts = [ac for ac in self.accounts if not (ac.get('account_name') == account_name)]
                print("Account was deleted successfully")
                return self.accounts
            else:
                return f'No account was deleted.'
        else:
            return "Account Not Found"
