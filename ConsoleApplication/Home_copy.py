
from User_copy import user
from Bank_copy import bank

main_user_dict={}
i=0

while(True):
    print("Enter the operation need to be performed:::")
    print("+-----------------------------+----------------------------+\n|                       Option|Operation                   |\n+-----------------------------+----------------------------+\n|                            1|Register                    |\n|                            2|Login                       |\n+-----------------------------+----------------------------+")

    choice=int(input())
    
    
    
    if(choice==1):
        
        users=user()
        main_user_dict[i]=users
        print(main_user_dict)
        print(main_user_dict[i].user_dict)
        print("Registered Successfully")
        i+=1

    elif(choice==2):
        user_name=str(input("Enter your user name: "))
        user_id=int(input("Enter your user id: "))
        password=str(input("Enter your password: "))
        user_obj=main_user_dict[user_id]
        log_flag=users.identify_user(user_name,password,user_obj)


        if(log_flag==1):

            print("""+-----------------------------+----------------------------+
            |                       Option|Operation                   |
            +-----------------------------+----------------------------+
            |                            1|Bank Accounts               |
            |                            2|Profile                     |
            |                            3|Invites                     |
            |                            4|Transactions                |
            |                            5|Help & Support              |
            |                            6|Pay                         |
            |                            7|Display all details         |
            |                            8|Logout                      |
            +-----------------------------+----------------------------+""")

            login_choice=str(input("Enter your Login option:::"))

            match login_choice:
                case '1':
                    # banks=bank()
                    print("""+-----------------------------+----------------------------+
                        |                       Option|Operation                   |
                        +-----------------------------+----------------------------+
                        |                            1|Add Account                 |
                        |                            2|Check Balance               |
                        |                            3|Add Money                   |
                        |                            4|Remove Account              |
                        |                            5|Go Back                     |
                        +-----------------------------+----------------------------+""")
                    
                    bank_choice=str(input("Enter your Bank option:::"))
                    bank_obj=bank()
                    bank_objs=user_obj.user_dict["Bank_details"]
                    match bank_choice:
                        
                        case '1':
                            id=len(bank_objs)
                            bank_objs[id]=bank()
                            print("Bank Account Added Successfully")
                                                   
                        case '2':
                            print(user_obj.user_dict["Bank_details"])
                            
                            for i in bank_objs.keys():
                                print(bank_objs[i])
                                print(bank_objs[i].bank_dict)
                                # bank_objs.check_balance(bank_objs)
                            # bank_id=int(input("Enter your bank id to check the balance of::: "))  
                            print("Balance Checked Successfully")

                        case '3':
                            # print("The bank accounts located in your account :::\n")
                            # for i in bank_objs.keys():
                            #     print("bank_id ::",i,"Bank details",bank_objs[i].bank_dict)

                            bank_obj.display_bank_details(bank_objs)
                            bank_id=int(input("Enter the bank s.no of the bank to add the money :::"))
                            print(bank_objs[bank_id].bank_dict)
                            amount=int(input("Enter the amount to be added::: "))
                            bank_objs[bank_id].bank_dict["bank_balance"]+amount                           

                            print("Money Added Successfully")

                        case '4':

                            print("Bank Account Removed Successfully")
                        case '5':
                            print("Going Back")
                        

                case '2':
                    print("""+-----------------------------+----------------------------+
                             |                       Option|Operation                   |
                             +-----------------------------+----------------------------+
                             |                            1|View Profile                |
                             |                            2|Edit Profile                |
                             |                            3|Go Back                     |
                             +-----------------------------+----------------------------+""")

                    profile_choice=str(input("Enter the profile option:::"))

                    match profile_choice:
                        case '1':
                            user_obj.display_user_details(user_obj)
                            print("\nUSER DETAILS DISPLAYED SUCCESSFULLY")
                        case '2':
                            user_obj.update_user_details(user_obj)
                            print(user_obj.user_dict)
                            print("\nUSER DETAILS UPDATED SUCCESSFULLY")
            print("Logged in")
        else:
            continue

    elif(choice==3):
        break