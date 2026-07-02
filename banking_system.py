#Name: ABDELRAHMAN MOHAMED ABDELMAGUD WAGIH
#TP NO: TP066717
#Super User Name: YoussefSA
#Password :01239876



#The Main Logic Fuction
def main_menu():
    while True:
        print(
        "*==================================================*\n"
        "| ---------Welcome to Abdelrahman's Bank Management------ |\n"
        "*==================================================*\n"
        "| =<< 1.            Open a new account         >>= |\n"
        "| =<< 2.                  login                >>= |\n"
        "| =<< 3.       Curnncey Converter Calculatour  >>= |\n"
        "| =<< 4.                Exit/Quit              >>= |\n"
        "*==================================================*\n"
    )


        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; ")


        if choiceNumber == "1":
            OPenAccMenu() # Open Account Menu  

        elif choiceNumber == "2":
            Login() 
        

        elif choiceNumber == "3":
            Currncy_Conv_Calc() #Currncy Converter Calculator 
            

        elif choiceNumber == "4":
            exit() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-4   |\n"
            "*===================*"
        )
        main_menu() 






#=======================================================================================================================================================================

#A Fuction That Displays The Open Account Menu
def OPenAccMenu():
    while True:
        print(
        "*==================================================*\n"
        "| ------- Welcome to Opening Account Menu -------- |\n"
        "*==================================================*\n"
        "| =<< 1.              Current Account          >>= |\n"
        "| =<< 2.              Saving Account           >>= |\n"
        "| =<< 3.            Return to Manin Menu       >>= |\n"
        "*==================================================*\n"
    )

        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            IOPenAcc() # Current Open Account 
        
        elif choiceNumber == "2":
            COPenAcc() # Saving Open Account

        elif choiceNumber == "3":
            main_menu() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-3   |\n"
            "*===================*"
        )
            return OPenAccMenu() 





#=======================================================================================================================================================================

#A Fuction That Open An Account For Saving Customer 
def SaVOPenAcc():
    print(
                "*=====================================*\n"
                "| -----Please Fill Up The Form------- |\n"
                "*=====================================*\n"
        )
    
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Enter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Email; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ") 
    AccType   = "SAV"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 100RM; "))
            break
        except ValueError:
            print("please Enter A valid Amount")
    while Amount_Diposit < 100:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 100RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Enter A valid Age")
        while age >= 18:
            with open ("Fourm.txt","a") as fh:
                recored = First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+str(Amount_Diposit)+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                    "*=======================================================================================================*\n"
                    "| -----Thank You For Filling Up The Form We Will Contact you in your email within 2 Busniss Days------- |\n"
                    "*=======================================================================================================*\n"
                )
            break
            
        else:
            print(
                "*==================================================*\n"
                "| -----You Are Too Young For Opening Account------- |\n"
                "*===================================================*"
            )
            
        




#========================================================================================================================================================================

#A Fuction That Open An Account For Current Customer 
def COPenAcc():
    print(
                "*=====================================*\n"
                "| -----Please Fill Up The Form------- |\n"
                "*=====================================*\n"
        )
    
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Email; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ") 
    AccType   = "CCU"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 500:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 500RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("Fourm.txt","a") as fh:
                recored = First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+str(Amount_Diposit)+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                    "*=======================================================================================================*\n"
                    "| -----Thank You For Filling Up The Form We Will Contact you in your email within 2 Busniss Days------- |\n"
                    "*=======================================================================================================*\n"
                )
            break
            
        else:
            print(
                "*==================================================*\n"
                "| -----You Are Too Young For Opening Account------- |\n"
                "*===================================================*"
            )
            
            
            
        


#=======================================================================================================================================================================

#A Fuction That Makes The Login Process
def Login():
    User_Name = input("\n=<< Enter Your User Name; ")
    Password  = input("=<< Enter Your PassWord; ")
    with open ("user_id & pass.txt","r") as fh:
        login_Details = "notfound"

        for recordline in fh:
            recoredlist = recordline.strip().split(";")
            if recoredlist[0] == User_Name and recoredlist[1] == Password:
                login_Details = recoredlist
                break

        if login_Details == "notfound":
            print(
                "*==================================================*\n"
                "| -- Incorrect User Name 0r password, try again -- |\n"
                "*==================================================*\n"
            )

        else:
            print(
                "*==============================*\n"
                "| -- Login successfull......-- |\n"
                "*==============================*\n"
            )
            if login_Details != "notfound":
                print(
         "\n*=================================================*\n"
        f"| --- Welcome to Abdelrahman's Bank: {login_Details[4]} ----- |\n"
         "*=================================================*\n"
                )

            if login_Details[9] == "SU":
                Spuer_User_Menu(login_Details) 

            elif login_Details[9] == "AU":
                Admin_Menu(login_Details) 

            elif login_Details[9] == "CCU":
                Cureent_Customer_Menu(login_Details) 

            elif login_Details[9] == "SAV":
                Sa_aCC_Menu(login_Details) # Saving Account Menu 

            else:
                print(
                "*==================================================*\n"
                "| -- Incorrect User Name 0r password, try again -- |\n"
                "*==================================================*\n"
            )
                return login_Details






#=======================================================================================================================================================================

#A Fuction That Displays The Super User Menu
def Spuer_User_Menu(login_Details):
    while True:
        print(
        "*==================================================*\n"
        "| ---------- Welcome to Super User Menu ---------- |\n"
        "*==================================================*\n"
        "| =<< 1.      Display All Pending Accounts     >>= |\n"
        "| =<< 2.           Add Admin Account           >>= |\n"
        "| =<< 3.      Add Current Customer Acount      >>= |\n"
        "| =<< 4.       Add Saving Customer Acount      >>= |\n"
        "| =<< 5.        Display All User Accounts      >>= |\n"
        "| =<< 6.          Change The Passsword         >>= |\n"
        "| =<< 7.          Change The User Name         >>= |\n"
        "| =<< 8.        Show All The TransAction       >>= |\n"
        "| =<< 9.           Return To Main Menu        >>= |\n"
        "| =<< 10.              Exit/Quit               >>= |\n"
        "*==================================================*\n"
    )
        

        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; ")

        if choiceNumber == "1":
            Display_All_Pending() 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "2":
            AddAdmin() 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "3":
            Add_CCU_ACC() #Add Current Customer User
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "4":
            Add_Sa_aCC() #Add Saving Customer User 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "5":
            Display_All_US() #Display All The Users 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "6":
            Change_Pass(login_Details)# Change The Password 


        elif choiceNumber == "7":
            Change_User_Name(login_Details) 

        elif choiceNumber == "8":
            Show_All_Trans() # Show All Users TransAction 
            return Spuer_User_Menu(login_Details) 


        elif choiceNumber == "9":
            return main_menu() 

        elif choiceNumber == "10":
            exit() 

        else:
             print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-10   |\n"
            "*===================*\n"
        )
        return Spuer_User_Menu() 
        




#=======================================================================================================================================================================

#A Fuction That Add A New Admin Account
def AddAdmin():
    user_id = genid("Admin User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Email; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "AU"
    loan = "-"
    Amount_Diposit  = "-"
    while True:
        try:
            age = float(input("=<< Please Enter your age; "))
            break
        except ValueError:
            print("please Ennter A valid Age")
    while age >= 18:
        with open ("user_id & pass.txt","a") as fh:
            recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
            fh.write(recored)
            print(
                    "*==============================================================*\n"
                    "| -------The Admin Account Has Been Added Successfully-------- |\n"
                    "*==============================================================*\n"
            )
        break
    
    else:
        print(
            "*==================================================*\n"
            "| -----You Are Too Young For Opening Account------- |\n"
            "*===================================================*"
        )
    


#=======================================================================================================================================================

#A Fuction That Add A New Saving Account
def Add_Sa_aCC():
    user_id = genid("Saving Customer User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Email; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "SAV"
    loan = "-"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 100RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 100:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 100RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 100RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("user_id & pass.txt","a") as fh:
                recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                        "*===============================================================*\n"
                        "| -------The Saving Account Has Been Added Successfully-------- |\n"
                        "*===============================================================*\n"
                )
            break
        
        else:
            print(
                "*==================================================*\n"
                "| -----You Are Too Young For Opening Account------- |\n"
                "*===================================================*"
            )





#=======================================================================================================================================================================

#A Fuction That Add A New Current Account
def Add_CCU_ACC():
    user_id = genid("Current Customer User") 
    user_pass = user_id
    print("User ID; ", user_id)
    print("User PassWord; ",user_pass)
    First_Name           = input("=<< Please Enter Your First Name; ")
    Last_Name            = input("=<< Please Enter Your Last Name; ")
    while True:
        try:
            Tele_No      = float(input("=<< Please Enter Your Telephone Number; "))
            break
        except ValueError:
            print("please Ennter A valid Telephone Number")
    city                 = input("=<< Please Enter Your City; ")
    email  = input("=<< Please Enter Your Email; ")
    while "@" not in email or ".com" not in email:
        email = input("=<< Please Enter A Valid Email; ")  
    AccType   = "CCU"
    loan = "-"
    while True:
        try:
            Amount_Diposit  =float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
            break
        except ValueError:
            print("please Ennter A valid Amount")
    while Amount_Diposit < 500:
        print(
                "*===========================================================*\n"
                "| -----For An Opening Account You Need Minimum 500RM------- |\n"
                "*===========================================================*"
            )
        try:
            Amount_Diposit  = float(input("=<< Please Enter Your Amount That You Want Deposit Minimum 500RM; "))
        except ValueError:
            print("please Ennter A valid Amount")

    else:
        while True:
            try:
                age = float(input("=<< Please Enter your age; "))
                break
            except ValueError:
                print("please Ennter A valid Age")
        while age >= 18:
            with open ("user_id & pass.txt","a") as fh:
                recored = user_id+";"+user_pass+";"+str(Amount_Diposit)+";"+loan+";"+First_Name+";"+Last_Name+";"+str(Tele_No)+";"+city+";"+email+";"+AccType+";"+str(age)+"\n"
                fh.write(recored)
                print(
                        "*================================================================*\n"
                        "| -------The Current Account Has Been Added Successfully-------- |\n"
                        "*================================================================*\n"
                )
            break
        
        else:
            print(
                "*==================================================*\n"
                "| -----You Are Too Young For Opening Account------- |\n"
                "*===================================================*"
            )
        
        



#=======================================================================================================================================================================

#A Fuction That Displays All The Users
def Display_All_US():
    allrec = []# = All Recored
    with open("user_id & pass.txt","r") as fh:
        for line in fh:
                allrec.append(line.strip().split(";"))
        print("="*157)
        print("|"+"Usre ID".center(10)+"|"+"User Password".center(15)+"|"+"Balance".center(15)+"|"+"Loan".center(10)+"|"+"First Name".center(15)+"|"+"Last Name".center(15)+"|"+"Tele No".center(15)+"|"+"City".center(10)+"|"+"Email".center(15)+"|"+"Account Type".center(15)+"|"+"Age".center(10)+"|")
        print("="*157)
        for cnt in range(0,len(allrec)): #cnt Counter
            print("|"+allrec[cnt][0].center(10)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(10)+"|"+allrec[cnt][4].center(15)+"|"+allrec[cnt][5].center(15)+"|"+allrec[cnt][6].center(15)+"|"+allrec[cnt][7].center(10)+"|"+allrec[cnt][8].center(15)+"|"+allrec[cnt][9].center(15)+"|"+allrec[cnt][10].center(10)+"|"+"\n")
        input("Press Enter to continue...\n")

                
    


#=======================================================================================================================================================================

#A Fuction That Displays All The Pendings Accounts Thats Need To be Opend
def Display_All_Pending():
    allrec = [] # = All Recored
    with open ("Fourm.txt","r") as fh:
        for line in fh:
            allrec.append(line.strip().split(";")) 
        print("="*124)
        print("|"+"First Name".center(15)+"|"+"Last Name".center(15)+"|"+"Tele No".center(15)+"|"+"City".center(15)+"|"+"Email".center(15)+"|"+"Balance".center(15)+"|"+"Account Type".center(15)+"|"+"Age".center(10)+"|")
        print("="*124)
        for cnt in range(0,len(allrec)): #cnt Counter
            print("|"+allrec[cnt][0].center(15)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(15)+"|"+allrec[cnt][4].center(15)+"|"+allrec[cnt][5].center(15)+"|"+allrec[cnt][6].center(15)+"|"+allrec[cnt][7].center(10)+"|"+"\n")
        input("Press Enter to continue...\n")
        




#=======================================================================================================================================================================

#A Fuction That Generate A New ID For A New Account
def genid(perm): # genid = Generate A New ID , Prem = premeter
    with open ("ID.txt","r") as IDfh:
        record = IDfh.readline()
        recordlist = record.strip().split(";")
        if perm == "Admin User":
            pref = "AU" #pref = Prefex 
            oldid = recordlist[0][2:]
        elif perm == "Current Customer User":
            pref = "CCU"
            oldid = recordlist[1][3:]
        elif perm == "Saving Customer User":
            pref = "SAV"
            oldid = recordlist[3][3:]
        nextid = int(oldid) + 1
        if len(str(nextid)) == 1:
            newid = "0000" + str(nextid)
        elif len(str(nextid)) == 2:
            newid = "000" + str(nextid)
        elif len(str(nextid)) == 3:
            newid = "00" + str(nextid)
        elif len(str(nextid)) == 4:
            newid = "0" +str(nextid)
        elif len(str(nextid)) == 5:
            newid = str(nextid)
        newid = pref + newid
        if perm == "Admin User":
            recordlist[0] = newid
        else:
            recordlist[1] = newid
        record = ";".join(recordlist)
        with open ("ID.txt","w") as fh:
            fh.write(record)
            return newid
            





#=======================================================================================================================================================================

#A Fuction That Displays The Admin Customer Menu
def Admin_Menu(login_Details):
    while True:
        print(
        "*==================================================*\n"
        "| ---------- Welcome to Admin User Menu ---------- |\n"
        "*==================================================*\n"
        "| =<< 1.      Add Current Customer Acount      >>= |\n"
        "| =<< 2.      Display All Pending Accounts     >>= |\n"
        "| =<< 3.          Change The Passsword         >>= |\n"
        "| =<< 4.          Change The User Name         >>= |\n"
        "| =<< 5.        Show All The TranAction        >>= |\n"
        "| =<< 6.       Add Saving Customer Acount      >>= |\n"
        "| =<< 7.           Return To Main Menu         >>= |\n"
        "| =<< 8.               Exit/Quit               >>= |\n"
        "*==================================================*\n"
    )
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            Add_CCU_ACC()#Add Current Customer User 
            return Admin_Menu(login_Details) 
        
        elif choiceNumber == "2":
            Display_All_Pending() 
            return Admin_Menu(login_Details) 
        
        elif choiceNumber == "3":
            Change_Pass(login_Details)# Change The Password 
            return Admin_Menu(login_Details) 

        elif choiceNumber == "4":
            Change_User_Name(login_Details) 
            return Admin_Menu(login_Details) 


        elif choiceNumber == "5":
            Show_All_Trans()# Show All Users TransAction 
            return Admin_Menu(login_Details) 


        elif choiceNumber == "6":
            Add_Sa_aCC() #Add Saving Customer User 
            return Admin_Menu(login_Details) 

        elif choiceNumber == "7":
            return main_menu() 

        elif choiceNumber == "8":
            exit() 

        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-8   |\n"
            "*===================*\n"
        )
            return Admin_Menu() 





#=======================================================================================================================================================================

#A Fuction That Calculate & Convert The RM into Diffrent Currency's
def Currncy_Conv_Calc():
    while True:
        print(
        "*==========================================================*\n"
        "| ---------- Curnncey Converter Calculatour Menu --------- |\n"
        "*==========================================================*\n"
        "| =<< 1.                    US Dollar                  >>= |\n"
        "| =<< 2.                  Kuwaiti dinar                >>= |\n"
        "| =<< 3.                      Euro                     >>= |\n"
        "| =<< 4.                Indonesian Rupiah              >>= |\n"
        "| =<< 5.                  chinese yuan                 >>= |\n"
        "| =<< 6.               Return To Main Menu             >>= |\n"
        "| =<< 7.                    Exit/Quit                  >>= |\n"
        "*==========================================================*\n"
    )
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")

        if choiceNumber == "1":
            Amount = float(input("Please Enter The You wan't to convert From RM To USD; "))
            result = Amount   * 0.24
            print(f"The Amount is; {result} $")

        elif choiceNumber == "2":
            Amount = float(input("Please Enter The You wan't to convert From RM To KD; "))
            result = Amount   * 0.072
            print(f"The Amount is; {result} KD")

        elif choiceNumber == "3":
            Amount = float(input("Please Enter The You wan't to convert From RM To EU; "))
            result = Amount   * 0.21
            print(f"The Amount is; {result} €")

        elif choiceNumber == "4":
            Amount = float(input("Please Enter The You wan't to convert From RM To IDR; "))
            result = Amount   * 3394.01
            print(f"The Amount is; {result} Rp")

        elif choiceNumber == "5":
            Amount = float(input("Please Enter The You wan't to convert From RM To CNY; "))
            result = Amount   * 1.50
            print(f"The Amount is; {result} ¥")

        elif choiceNumber == "6":
            main_menu() 

        elif choiceNumber == "7":
            exit() 
            
        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-7   |\n"
            "*===================*\n"
        )
        Currncy_Conv_Calc() 

    




#=======================================================================================================================================================================

#A Fuction That Displays The Current Customer Menu
def Cureent_Customer_Menu(login_Details):
    while True:
        print(
        "*=====================================================*\n"
        "| ---------- Welcome to Customer User Menu ---------- |\n"
        "*=====================================================*\n"
        "| =<< 1.             Withdrawing Money            >>= |\n"
        "| =<< 2.             Depositing Money             >>= |\n"
        "| =<< 3.            Display My Details            >>= |\n"
        "| =<< 4.           Change The Password            >>= |\n"
        "| =<< 5.             Report Statement             >>= |\n"
        "| =<< 6.             Return To Main Menu          >>= |\n"
        "| =<< 7.                 Exit/Quit                >>= |\n"
        "*=====================================================*\n"
    )
    
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")


        if choiceNumber == "1":
            WithDrraw(login_Details) 
            

        elif choiceNumber == "2":
            Deposit(login_Details) 

        elif choiceNumber == "3":
            Display_Details(login_Details) 

        elif choiceNumber == "4":
            Change_Pass(login_Details) 

        elif choiceNumber == "5":
            Report(login_Details) 

        elif choiceNumber == "6":
            return main_menu() 

        elif choiceNumber == "7":
            exit() 


        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-7   |\n"
            "*===================*\n"
        )
            Cureent_Customer_Menu() 

       





#=======================================================================================================================================================================

#A Fuction That Display's All Account Details
def Display_Details(login_Details):
    allrec = []
    with open("user_id & pass.txt","r") as fh:
        for line in fh:
                allrec.append(line.strip().split(";"))
        print("="*157)
        print("|"+"Usre ID".center(10)+"|"+"User Password".center(15)+"|"+"Balance".center(15)+"|"+"Loan".center(10)+"|"+"First Name".center(15)+"|"+"Last Name".center(15)+"|"+"Tele No".center(15)+"|"+"City".center(10)+"|"+"Email".center(15)+"|"+"Account Type".center(15)+"|"+"Age".center(10)+"|")
        print("="*157)
        for cnt in range(0,len(allrec)):
            if (login_Details[0] == allrec[cnt][0]) :
                    print("|"+allrec[cnt][0].center(10)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(10)+"|"+allrec[cnt][4].center(15)+"|"+allrec[cnt][5].center(15)+"|"+allrec[cnt][6].center(15)+"|"+allrec[cnt][7].center(10)+"|"+allrec[cnt][8].center(15)+"|"+allrec[cnt][9].center(15)+"|"+allrec[cnt][10].center(10)+"|"+"\n")
        input("Press Enter to continue...")




#=======================================================================================================================================================================

#A Fuction That Display's The Saving Account Menu
def Sa_aCC_Menu(login_Details):
    while True:
        print(
        "*============================================================*\n"
        "| ---------- Welcome to Saving Customer User Menu ---------- |\n"
        "*============================================================*\n"
        "| =<< 1.                 Depositing Money                >>= |\n"
        "| =<< 2.                 withdrawl  Money                >>= |\n"
        "| =<< 3.                 Display My Details              >>= |\n"
        "| =<< 4.                Change The Password              >>= |\n"
        "| =<< 5.                  Report Statement               >>= |\n"
        "| =<< 6.                Return To Main Menu              >>= |\n"
        "| =<< 7.                    Exit/Quit                    >>= |\n"
        "*============================================================*\n"
    )
    
        choiceNumber = input("=<< Select Your Choice Number From The Above Menu; \n")



        if choiceNumber == "1":
            Deposit(login_Details) 

        elif choiceNumber == "2":
            WithDrraw(login_Details) 


        elif choiceNumber == "3":
            Display_Details() 


        elif choiceNumber == "4":
            Change_Pass(login_Details) 


        elif choiceNumber == "5":
            Report(login_Details) 


        elif choiceNumber == "6": 
            main_menu() 


        elif choiceNumber == "7":
            exit() 


        else:
            print(
            "*===================*\n"
            "| Invalid option    |\n"
            "| Choose from 1-7   |\n"
            "*===================*\n"
        )
            return Sa_aCC_Menu() 





#=======================================================================================================================================================================

#A Fuction That Make The Withdraw TransAction For The Customers
def WithDrraw(login_Details):
    allrec = []# = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        while True:
            try:
                balance = float(input("=<< Please Enter The Amount you want to Withdraw; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt #cnt = Counter
                    break
        if balance < float(allrec[ind][2]):
            old_balance = allrec[ind][2]
            New_amount = float(old_balance) - balance
            allrec[ind][2] = str(New_amount)
            with open("user_id & pass.txt","w") as fh:
                    nor = len(allrec)
                    for cnt in range(0,nor):
                        rec = ";".join(allrec[cnt])+"\n"
                        fh.write(rec)
                    print(
                "*==============================================*\n"
                "| -----Your Have withdrawed Succsefully------- |\n"
                "*==============================================*\n")
                    print(
                "*===================================================*\n"
                f"| -----Your Balance Now Is {allrec[ind][2]}------- |\n"
                "*===================================================*\n")
                    with open("Transaction.txt", "a") as fh:
                            Withdraw = str(balance)
                            money = str(New_amount)
                            ID = str(allrec[ind][0])
                            with open("Transaction.txt", "a") as fh:
                                rec = "Withdraw"";""-"+Withdraw+";"+money+";"+ID+";"+date+"\n"
                                fh.write(rec)
                        
        else:
            print(
                "*==================================================*\n"
                "| ------------You don't Have Enogh Money----------- |\n"
                "*===================================================*"
            )
            return WithDrraw(login_Details)
        




#=======================================================================================================================================================================

#A Fuction That Make The Deposit TransAction For The Customers
def Deposit(login_Details):
    allrec = [] # = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:#Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        while True:
            try:
                balance = float(input("=<< Please Enter The Amount you want to Deposit; "))
                break
            except ValueError:
                print("=<< Please Enter A Valid Amount =>>")
        date = input("=<< Please Enter The Date in This Format dd/mm/yyyy; ")
        while "/" not in date:
            date = input("=<< Please Enter A A Valid Date in This Format dd/mm/yyyy; ")
        ind = -1#ind = index
        nor = len(allrec)#nor = Number of The Recoreds
        for cnt in range(0,nor): #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        if balance < 10000:
            old_balance = allrec[ind][2]
            New_amount = float(old_balance) + balance
            allrec[ind][2] = str(New_amount)
            with open("user_id & pass.txt","w") as fh:
                    nor = len(allrec)
                    for cnt in range(0,nor):
                        rec = ";".join(allrec[cnt])+"\n"
                        fh.write(rec)
                    print(
                "*==============================================*\n"
                "| -------Your Have Diposit Succsefully-------- |\n"
                "*==============================================*")
                    print(
                "*===================================================*\n"
                f"| -----Your Balance Now Is {allrec[ind][2]}------- |\n"
                "*===================================================*\n")
                    with open("Transaction.txt", "a") as fh:
                                Deposite = str(balance)
                                money = str(New_amount)
                                ID = str(allrec[ind][0])
                                with open("Transaction.txt", "a") as fh:
                                    rec = "Deposit"";""+"+Deposite+";"+money+";"+ID+";"+date+"\n"
                                    fh.write(rec)
                        
        else:
            print(
                "*=========================================================*\n"
                "| -------You Can't deposit more than 10000 RM a Day------- |\n"
                "*=========================================================*")
            return Deposit(login_Details)





#=======================================================================================================================================================================

#A Fuction That Change The Password For The Super, Admin and Customer Users
def Change_Pass(login_Details):
    allrec = []# = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh:#Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        newpass = input("=<< Please Enter The new Password; ")
        ind = -1 #ind = index
        nor = len(allrec)#nor = Number of The Recoreds
        for cnt in range(0,nor):  #cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        
        allrec[ind][1] = newpass
        with open("user_id & pass.txt","w") as fh:
                nor = len(allrec)
                for cnt in range(0,nor):
                    rec = ";".join(allrec[cnt])+"\n"
                    fh.write(rec)
                print(
            "*====================================================================*\n"
            "| ------------Your Password Have Been Changed Succsefully----------- |\n"
            "*====================================================================*"
                )





#=======================================================================================================================================================================

#A Fuction That Change The User Name Avilibale Only For The Super And Admin User
def Change_User_Name(login_Details):
    allrec = []# = All Recored
    with open ("user_id & pass.txt","r") as fh:
        for rec in fh: #Rec = Recored
                  reclist = rec.strip().split(";")
                  allrec.append(reclist)
        newpass = input("=<< Please Enter The New User Name; ")
        ind = -1 #ind = index
        nor = len(allrec) #nor = Number of The Recoreds
        for cnt in range(0,nor):  #Cnt = Counter
                if login_Details[0] == allrec[cnt][0]:
                    ind = cnt
                    break
        
        allrec[ind][0] = newpass
        with open("user_id & pass.txt","w") as fh:
                nor = len(allrec)
                for cnt in range(0,nor):
                    rec = ";".join(allrec[cnt])+"\n"
                    fh.write(rec)
                print(
            "*=================================================================*\n"
            "| ------------Your User Name Have Changed Succsefully------------ |\n"
            "*=================================================================*"
        )



  
                
        
                    


#=======================================================================================================================================================================

#A Fuction That Diplays For Customer His Transactions 
def Report(login_Details):
    allrec = [] # = All Recored
    with open("Transaction.txt","r") as fh:
        for line in fh:
            allrec.append(line.strip().split(";"))
    print("="*85)
    print("Type OF Transaction".center(30)+"|"+"Amount".center(15)+"|"+"Balance".center(15)+"|"+"User ID".center(15)+"|"+"Date Of Tranaction".center(20)+"|")
    print("="*85)
    for cnt in range(0,len(allrec)):  #cnt = Counter
        if (login_Details[0] == allrec[cnt][3]):
            print(allrec[cnt][0].center(30)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(15)+"|"+allrec[cnt][4].center(20)+"|")
    input("Press Enter to continue...")
        




#=======================================================================================================================================================================

#A Fuction That Show All the transacrions of Customer
def Show_All_Trans():
    with open("Transaction.txt","r") as fh:
        print("="*85)
        print("Type OF Transaction".center(30)+"|"+"Amount".center(15)+"|"+"Balance".center(15)+"|"+"User ID".center(15)+"|"+"Date Of Tranaction".center(20)+"|")
        print("="*85)
        for cnt in fh:  #cnt = Counter
            allrec = cnt.strip().split(";")
            print(allrec[cnt][0].center(30)+"|"+allrec[cnt][1].center(15)+"|"+allrec[cnt][2].center(15)+"|"+allrec[cnt][3].center(15)+"|"+allrec[cnt][4].center(20)+"|")
    input("Press Enter to continue...")










main_menu() 




























































































#Good By No Of The Line
