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
    

    def identify_user(self,user_name,user_password,user_obj):
        self.user_name=user_name
        self.user_password=user_password
        self.user_obj=user_obj
        log_flag=False

        if(user_name==self.user_obj.user_name):
            if(self.user_obj.password==user_password):
                log_flag=True
                print(self.user_obj.user_name,self.user_obj.password,self.user_obj)
                print("login successful")
            else:
                print("incorrect password")
        else:
            print("invalid user_id")

        return log_flag
    

    def update_user_details(self,user_obj):
        self.user_obj=user_obj
        self.user_obj.user_dict["user_name"]=str(input("Enter your user name:::  ::"))
        self.user_obj.user_dict["password"]=str(input("Enter your password: "+self.user_obj.password+" ::"))
        self.user_obj.user_dict["email"]=str(input("Enter your email: "+self.user_obj.email+" ::"))
        self.user_obj.user_dict["preferred_lang"]=str(input("Enter your prefered language: "+self.user_obj.prefered_lang+" ::"))               

        self.user_obj.user_dict["push_notification"]=str(input("do you want to enable push notification: "+self.user_obj.push_notification+" ::"))
        self.user_obj.user_dict["email_notification"]=str(input("do you want to enable email notification: "+self.user_obj.email_notification+" ::"))

        self.user_obj.user_dict["referel_code"]="self.user_obj.referel_code"
        
        ''' self.user_obj]={"user_name":self.user_name,"password":self.password,"email":self.email,"preferred_lang":self.prefered_lang,\
            "referel_code":self.referel_code,"push_notification":self.push_notification,"email_notification":self.email_notification,"Bank_details":[]}
         '''
        return self.user_obj


    def display_user_details(self,user_obj):
        print(self.user_obj.user_dict["user_name"])
        # print(self.user_dict["password"])
        print(self.user_obj.user_dict["email"])
        print(self.user_obj.user_dict["preferred_lang"])
        print(self.user_obj.user_dict["referel_code"])
        print(self.user_obj.user_dict["push_notification"])
        print(self.user_obj.user_dict["email_notification"])
        print(self.user_obj.user_dict["Bank_details"])
