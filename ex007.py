class BankAccount:
    def __init__(self, initial_balance=0):
        self._initial_balance = initial_balance
        self.type = 'BankAccount'

    @property
    def balance(self):
        return self._initial_balance

    def deposit(self, value):
        if value <= 0:
            raise ValueError("Only numbers higher than 0 are allowed.")
        self._initial_balance+=value
        print(f'Deposited ${value:.2f}.')

    def withdraw(self, value):
        if value <= 0 or value > self._initial_balance:
            raise ValueError("Only numbers higher than 0 are allowed.")
        self._initial_balance-=value
        print(f'Withdrew ${value:.2f}.')

    def __repr__(self):
        return f'A {self.type} with ${self._initial_balance:.2f} in it.'


class Savings(BankAccount):
    def __init__(self, ib=0):
        super().__init__(ib)
        self.type = 'SavingsBankAccount'
        self.interest_rate = 0.0035

    def PayInterest(self):
        self.deposit(self._initial_balance*self.interest_rate)


class HighInterest(Savings):
    def __init__(self, ib=0, withdraw_fee=5):
        super().__init__(ib)
        self.type = 'HighInterestBankAccount'
        self.withdraw_fee = withdraw_fee
        self.interest_rate = 0.007

    def withdraw(self, value):
        if 0 < value + self.withdraw_fee <= self._initial_balance:
            self._initial_balance -= self.withdraw_fee
            super().withdraw(value)


class LockedIn(HighInterest):
    def __init__(self, ib=0, withdraw_fee=5):
        super().__init__(ib, withdraw_fee)
        self.type = 'LockedInBankAccount'
        self.interest_rate = 0.009

    def withdraw(self, value):
        print("Unable to withdraw early on a LockedIn account")
