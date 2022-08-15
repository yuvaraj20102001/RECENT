

class bank:
    def __init__(self):
        self.bank_dict={}
        self.account_number=str(input("Enter your account number: "))
        self.ifsc=str(input("Enter your ifsc: "))
        self.display_name=str(input("Enter your display name: "))
        self.bank_name=str(input("Enter your bank name: "))
        self.bank_balance=int(input("Enter your bank balance: "))
        self.upi=str(input("Enter your upi: "))
        self.bank_dict={"account_number":self.account_number,"ifsc":self.ifsc,"display_name":self.display_name,\
            "bank_name":self.bank_name,"bank_balance":self.bank_balance,"upi":self.upi}
        
        
    def add_money(self,bank_obj,amount):
        self.bank_obj=bank_obj
        self.amount=amount
        self.bank_obj.bank_dict["bank_balance"]+=self.amount


    def check_balance(self,bank_obj):
        self.bank_obj=bank_obj
        print(self.bank_obj.bank_dict["bank_balance"])

    def display_bank_details(self,bank_objs):
        self.bank_objs=bank_objs
        print("The bank accounts located in your account :::\n")
        for i in self.bank_objs.keys():
            print("bank_id ::",i,"Bank details",self.bank_objs[i].bank_dict)
        

        