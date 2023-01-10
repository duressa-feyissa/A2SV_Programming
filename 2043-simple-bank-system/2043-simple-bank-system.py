class Bank:

    accounts = {}
    no_of_account = 1
    def __init__(self, balance: List[int]):
        self.total = len(balance)
        for initial in balance:
            self.accounts[self.no_of_account] = initial
            self.no_of_account += 1
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.total and 1 <= account2 <= self.total:
            if self.accounts[account1] >= money:
                self.accounts[account1] -= money
                self.accounts[account2] += money
                return True
            
    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.total:
            self.accounts[account] += money
            return True

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.total:
            if self.accounts[account] >= money:
                self.accounts[account] -= money
                return True