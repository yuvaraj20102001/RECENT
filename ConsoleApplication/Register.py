

class Register:

    main_dict={}
    
    def __init__(self):
        pass
    

    def get_user_details(self):
        self.user_name=str(input("Enter your user name: "))
        self.password=str(input("Enter your password: "))
        self.email=str(input("Enter your email: "))
        self.prefered_lang=str(input("Enter your prefered language: "))
        self.referel_code=str(input("Enter your referel code: "))
                   

        self.push_notification=str(input("do you want to enable push notification: "))
        self.email_notification=str(input("do you want to enable email notification: "))

        self.main_dict[self.user_name]=[self.password,self.email,self.prefered_lang,self.referel_code,self.push_notification,self.email_notification,[]]
        self.bank_flag=int(input("Enter 1 if you want to add a bank account else 0: "))
    
        if(self.bank_flag==1):
            Bank.get_bank_details() 


    def display(self):
        print(self.user_name)
        print(self.password)
        print(self.email)
        print(self.prefered_lang)
        print(self.referel_code)
        print(self.push_notification)
        print(self.email_notification)

    def identify_user(self,user_name,password):
        self.user_name=user_name
        self.password=password

        if(user_name in self.main_dict):
            if(password==self.main_dict[user_name][0]):
                log_flag=1
            else:
                log_flag=0
        else:
            log_flag=0

        return log_flag
    
    def get_main_dict(self):
        return self.main_dict

    def set_main_dict(self,main_dict):
        self.main_dict=main_dict
        
    def get_user_name(self):
        return self.user_name

class Bank(Register):
    
    def __init__(self):
        pass

        # main_dict=Register.get_main_dict(self)
        # user_name=Register.get_user_name(self)

        # self.set_main_dict(self,main_dict[user_name].append(bank_list))
    def get_bank_details(self):
        self.account_number=str(input("Enter your account number: "))

        self.ifsc=str(input("Enter your IFSC: "))
        self.display_name=str(input("Enter your display name: "))
        self.bank_name=str(input("Enter your bank name: "))
        self.bank_balance=str(input("Enter your bank balance: "))
        self.upi=str(input("Enter your UPI: "))

        bank=[self.account_number,self.ifsc,self.display_name,self.bank_name,self.bank_balance,self.upi]
    
        self.main_dict[self.user_name][-1].append(bank)
        print(self.main_dict)
    
   

    def check_balance(self):
        print("Account Balance")
        print(self.main_dict)

    def add_money(self):
        print("Enter amount to add")
        amount=int(input())
        self.main_dict[self.user_name][-1][4]+=amount
        print("Amount added successfully")
    def remove_account(self):
        print(self.main_dictf)
        print("Enter the s.no of the account to be removed :::")
        x=int(input())
        Register.main_dict[self.user_name][-1][x].pop()
        print("Account removed successfully")


    def display(self):
        print(self.account_number)
        print(self.ifsc)
        print(self.display_name)
        print(self.bank_name)
        print(self.bank_balance)
        print(self.upi)