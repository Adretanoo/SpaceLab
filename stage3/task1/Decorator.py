class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

class AccountDecorator:
    def __init__(self, account):
        self._account = account

    def get_balance(self):
        return self._account.get_balance()

class VIPAccount(AccountDecorator):
    def get_balance(self):
        return self._account.get_balance() + 100

account = BankAccount(1000)
print(account.get_balance())

vip_account = VIPAccount(account)
print(vip_account.get_balance())
