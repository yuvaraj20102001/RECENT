from Register import Register
from Register import Bank
# from Bank_accounts import Bank_operations
while(True):
    print("Enter the opetion need to be performed:::")
    print("1. Register")
    print("2. Login")

    choice=int(input())


    if(choice==1):
        reg=Register()
        reg.get_user_details()

    if(choice==2):
        log_user_name=str(input("Enter your user name: "))
        log_password=str(input("Enter your password: "))
        log_flag=reg.identify_user(log_user_name,log_password)

        if(log_flag):
            print("Login Successful")
            print("1.bank accounts\n2.profiles\n3.invites\n4.transactions\n5.help and support\n6.pay\n7.display all details\n8.logout")
            log_bank=Bank()

            log_choice=int(input())

            if(log_choice==1):
                print("1.Adda bank account\n2.Check balance\n 3.Add money\n4.remove account\n 5.Go back")
                log_choice_1=int(input())
                if(log_choice_1==1):
                    log_bank.get_bank_details()

                if(log_choice_1==2):
                    log_bank.check_balance()

            if(log_choice==2):
                print("view profile\nedit profile\nlogout")
                log_bank.get_user_details()
                


        else:
            print("Login Unsuccessful")



