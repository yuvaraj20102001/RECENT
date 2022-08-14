from Register import Register

'''     1.bank accounts 
        2.profiles
        3.invites
        4.transactions
        5.help and support
        6.pay
        7.display all details
        8.logout                        '''

# print("1.Adda bank account\n2.Check balance\n 3.Add money\n4.remove account\n 5.Go back")
class Bank_operations:
    
    def __init__(self,account_number,ifsc,display_name,bank_name,bank_balance,upi):
        self.account_number=account_number
        self.ifsc=ifsc
        self.display_name=display_name
        self.bank_name=bank_name
        self.bank_balance=bank_balance
        self.upi=upi
        bank_list=[self.account_number,self.ifsc,self.display_name,self.bank_name,self.bank_balance,self.upi]

        Register.main_dict[Register.user_name].append(bank_list)
    
    def check_balance(self,user_name):
        print(Register.main_dict[user_name][-1][4])

    def add_money(self,user_name):
        print("Enter amount to add")
        amount=int(input())
        Register.main_dict[user_name][-1][4]+=amount
        print("Amount added successfully")

    def remove_account(self,user_name):
        x=int(input("enter the s.no of the account to be removed :::"))
        Register.main_dict[user_name][-1][x-1].pop()
        print("Account removed successfully")




    