class BankAccount:

    def __init__(self, name, balance, currency):
        self.name = name
        self.balance = balance
        self.currency = currency
        self.account_history = ['Account was created']

    def deposit(self, amount):
        if amount < 0:
            raise ValueError
        else:
            self.balance += amount
            self.account_history.append('Deposited {}{}'.format(amount, self.currency))


    def __int__(self):
        self.account_history.append('__int__ chek -> {}{}'.format(self.balance, self.currency))
        return self.balance

    def balance(self):
        balance_history = 'Balance check -> ' + str(self.balance) + self.currency
        self.account_history.append(balance_history)
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            self.account_history.append('{}{} was withdrawed'.format(amount, self.currency))
            return True
        else:
            self.account_history.append('Withdraw for {}{} failed.'.format(amount, self.currency))
            return False

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)


    def transfer_to(self, account, amount):
        if self.currency != account.currency:
            raise ValueError
        if amount > self.balance:
            raise ValueError

        account.account_history.append('Transfer from {} for {}{}'.format(self.name, amount, self.currency))
        self.account_history.append('Transfer to {} for {}{}'.format(account.name, amount, self.currency))
        account.balance = account.balance + amount
        self.balance = self.balance - amount
        return True

    def history(self):
        return self.account_history
