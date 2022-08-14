

class bank:
    def __init__(self):
        pass

    def get_bank_details(self,bank_id):
        self.bid=bank_id
        bank_dict={}
        self.account_number=str(input("Enter your account number: "))
        self.ifsc=str(input("Enter your ifsc: "))
        self.display_name=str(input("Enter your display name: "))
        self.bank_name=str(input("Enter your bank name: "))
        self.bank_balance=int(input("Enter your bank balance: "))
        self.upi=str(input("Enter your upi: "))
        bank_dict[self.bid]={"account_number":self.account_number,"ifsc":self.ifsc,"display_name":self.display_name,\
            "bank_name":self.bank_name,"bank_balance":self.bank_balance,"upi":self.upi}
        
        return bank_dict


    def check_balance(self):
        print()
        

        