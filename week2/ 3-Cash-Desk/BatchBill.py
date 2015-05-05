from Bill import Bill


class BatchBill(Bill):

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __int__(self):
        return self.total()

    def total(self):
        return sum([int(bill) for bill in self.bills])

    def __getitem__(self, index):
        return self.bills[index]
