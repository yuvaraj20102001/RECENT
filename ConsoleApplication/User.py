
from Bank import bank

class user:
    
    def __init__(self):
        pass
    user_dict={}
    def get_user_details(self,i):
        self.uid=i
        self.user_name=str(input("Enter your user name: "))
        self.password=str(input("Enter your password: "))
        self.email=str(input("Enter your email: "))
        self.prefered_lang=str(input("Enter your prefered language: "))
        self.referel_code=str(input("Enter your referel code: "))           

        self.push_notification=str(input("do you want to enable push notification: "))
        self.email_notification=str(input("do you want to enable email notification: "))

        self.user_dict[self.uid]={"user_name":self.user_name,"password":self.password,"email":self.email,\
            "preferred_lang":self.prefered_lang,"referel_code":self.referel_code,\
            "push_notification":self.push_notification,"email_notification":self.email_notification,"Bank_details":[]}
        
        self.bank_flag='y'
        bank_id=0
        while(self.bank_flag=='y'):
        
            self.bank_flag=str(input("Enter y if you want to add a bank account else n: "))
            match self.bank_flag:
                case "y":
                    bank_reg=bank()
                    self.bank_details=bank_reg.get_bank_details(bank_id)
                    bank_id+=1
                    self.user_dict[self.uid]["Bank_details"].append(self.bank_details)
                case "n":
                    self.bank_details={}
        
      


        return self.user_dict
        # self.bank_flag=int(input("Enter 1 if you want to add a bank account else 0: "))





    

    def update_user_details(self,i):
        self.uid=i
        self.user_name=str(input("Enter your user name::: "+self.user_dict[self.uid]["user_name"]+" ::"))
        self.password=str(input("Enter your password: "+self.user_dict[self.uid]["password"]+" ::"))
        self.email=str(input("Enter your email: "+self.user_dict[self.uid]["email"]+" ::"))
        self.prefered_lang=str(input("Enter your prefered language: "+self.user_dict[self.uid]["preferred_lang"]+" ::"))               

        self.push_notification=str(input("do you want to enable push notification: "+self.user_dict[self.uid]["push_notification"]+" ::"))
        self.email_notification=str(input("do you want to enable email notification: "+self.user_dict[self.uid]["email_notification"]+" ::"))

        self.referel_code=self.user_dict[self.uid]["referel_code"]
        
        self.user_dict[self.uid]={"user_name":self.user_name,"password":self.password,"email":self.email,"preferred_lang":self.prefered_lang,\
            "referel_code":self.referel_code,"push_notification":self.push_notification,"email_notification":self.email_notification,"Bank_details":[]}
        
        return self.user_dict[self.uid]




    def identify_user(self,user_name,user_password,user_id):
        self.user_name=user_name
        self.user_password=user_password
        self.user_id=user_id
        log_flag=False

        if(self.user_id in self.user_dict):
            if(self.user_password==self.user_dict[self.user_id]["password"]):
                print("Login Successful")
                log_flag=True
            else:
                print("invalid password")
                log_flag=False

        else:
            print("invalid user id")
            log_flag=False

        return log_flag

    def display_user_details(self,user_id):
        self.user_id=user_id

        print(self.user_dict[self.user_id]["user_name"])
        # print(self.user_dict[self.user_id]["password"])
        print(self.user_dict[self.user_id]["email"])
        print(self.user_dict[self.user_id]["preferred_lang"])
        print(self.user_dict[self.user_id]["referel_code"])
        print(self.user_dict[self.user_id]["push_notification"])
        print(self.user_dict[self.user_id]["email_notification"])
        print(self.user_dict[self.user_id]["Bank_details"])
