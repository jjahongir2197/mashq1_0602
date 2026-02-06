class Transaction:
    def __init__(self, t_type, amount):
        self.t_type = t_type
        self.amount = amount


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(Transaction("Kirim", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(Transaction("Chiqim", amount))
        else:
            print("Balans yetarli emas")

    def transfer(self, other, amount):
        if amount <= self.balance:
            self.withdraw(amount)
            other.deposit(amount)
        else:
            print("Pul yetarli emas")

    def report(self):
        print(f"\n{self.owner} | Balans: {self.balance}")
        for h in self.history:
            print(h.t_type, h.amount)


acc1 = BankAccount("Jahongir", 5000000)
acc2 = BankAccount("Ali", 2000000)

acc1.transfer(acc2, 700000)
acc1.deposit(300000)
acc1.report()
acc2.report()
