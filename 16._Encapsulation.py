class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass

acc=Account("123","arya123")
print(acc.acc_no)
print(acc.acc_pass)