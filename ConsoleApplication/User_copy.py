from Bank_copy import bank


class user:
    
    def __init__(self):
        
        
        self.user_name=str(input("Enter your user name: "))
        self.password=str(input("Enter your password: "))
        self.email=str(input("Enter your email: "))
        self.prefered_lang=str(input("Enter your prefered language: "))
        self.referel_code=str(input("Enter your referel code: "))           

        self.push_notification=str(input("do you want to enable push notification: "))
        self.email_notification=str(input("do you want to enable email notification: "))

        self.user_dict={"user_name":self.user_name,"password":self.password,"email":self.email,\
            "preferred_lang":self.prefered_lang,"referel_code":self.referel_code,\
            "push_notification":self.push_notification,"email_notification":self.email_notification,"Bank_details":{}} 
        
        self.bank_flag='y'
        bank_id=0
        while(self.bank_flag=='y'):
        
            self.bank_flag=str(input("Enter y if you want to add a bank account else n: "))
            match self.bank_flag:
                case "y":
                    bank_reg=bank()
                    self.user_dict["Bank_details"][bank_id]=bank_reg
                    bank_id+=1
                    
                    print("account added")
                