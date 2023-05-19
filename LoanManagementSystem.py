#FAIZAN SAMDANI
#TP062706

#Function for the main menu of the Malaysian Bank
def mainmenu():
    mb_exit=False   #A defined variable to loop
    while mb_exit==False:   #While loop for incorrect input
        print("""

Welcome to Malaysia Bank""")


        print("""
The 3 types of users are:
1. Admin
2. New Customer
3. Registered Customer
4. Exit""")


        user=int(input("Enter the user type: "))
            
        if user==1:
            admin()

        elif user==2:
            nc()
            
        elif user==3:
            rc()

        elif user==4:
            exit()

        else:
            print("""
Incorrect input""")
            continue


#Function to call whenever there's an exit that checks if the input entered is correct
def back():
    exit=input("Enter q to exit: ") 
    if exit=="q":
        return "exit"
    else:
        while exit!="q":
            print("Incorrect input")
            exit=input("Enter q to exit: ")
        return "exit"


#Function to make sure the username entered by a user while registering is unique
def username_check():
    username_loop=True
    while username_loop==True:  #While loop to keep repeating till the username is unique
        with open("NewCustomer.txt", "r+") as pending, open("RegisteredCustomer.txt", "r") as approved, open("RejectedCustomer.txt", "r") as rejected:

            mb_userid=input("Enter your username: ")
            username_exists=False   #Variable is false while a username is unique

            for line1 in pending:   
                pendinglist=line1.split()
                if mb_userid==pendinglist[1]:   #Checking if the username is the same as the second element in each line in the file
                    username_exists=True    #When the username is found in a file the variable changes to true

            for line2 in approved:
                approvedlist=line2.split()
                if mb_userid==approvedlist[1]:
                    username_exists=True

            for line3 in rejected:
                rejectedlist=line3.split()
                if mb_userid==rejectedlist[1]:
                    username_exists=True

        if username_exists==True:
            print("Username already exists, please try again")
            continue    #If username is found to exist the loop restarts
        else:
            break   #If username does not exist the loop breaks
    
    return mb_userid    #The unique username is returned back to the user


#Function to check if the user is admin or not
def admin():
    admin_user=input("Enter username: ")
    admin_pw=input("Enter password: ")
       
    if admin_user=="admin" and admin_pw=="1234":    #Check if the username and password entered by the user matches with admin details or not
        user_admin=True
            
    else:
        user_admin=False

    while user_admin==False:    #Loop to run till the details entered by the user matches the admin detials
        print("Incorrect uername or password")
        admin_retry=input("Press any key to retry or 2 to exit: ")
        if admin_retry=="2":    #Gives an option for the user to exit
            mainmenu()
        else:
            admin_user=input("Enter username: ")
            admin_pw=input("Enter password: ")

            if admin_user=="admin" and admin_pw=="1234":
                user_admin=True

            else:
                continue
            
    admin_f()


#Function to give admin options for admin functionalities
def admin_f():
    admin_exit=False
    while admin_exit==False:
        print("""
Welcome Admin""")
        
        print("""
Your options are:
1.View the new customer’s registration request
2.Give approval to new customer to access system with their login id and password
3.Provide unique LoanID to registered customer
4.Can view all transactions of specific customer
5.Can view all transactions of specific Loan type (EL/CL/HL/PL)
6.Can view all transaction of all customer
7.Can view all transaction of all types Loan
8.Exit""")
        
        admin_function=int(input("What would you like to do?: "))

        if admin_function==1:
            admin_f1()

        elif admin_function==2:
            admin_f2()

        elif admin_function==3:
            admin_f3()

        elif admin_function==4:
            admin_f4()

        elif admin_function==5:
            admin_f5()

        elif admin_function==6:
            admin_f6()

        elif admin_function==7:
            admin_f7()

        elif admin_function==8:
            mainmenu()

        else:   #If the input entered by admin is incorrect the loop restarts
            print("""
Incorrect Input""")
            continue


#Function to let admin view all the registration requests
def admin_f1():
    with open("NewCustomer.txt", "r") as regreq:
        req=regreq.read()
        print(req)
        if back()=="exit":
            admin_f()
            

#Function to let admin approve or reject pending registration requests
def admin_f2():
    with open("NewCustomer.txt", "r+") as register:
        for line in register:   
            print(line)
            registerlist=line.split()
            exitfileloop=False
            while exitfileloop==False:
                adminapproval=int(input("""
Press 1 to accept or 2 to reject: """))

                if adminapproval==1:
                    newline=line.replace("ApprovalPending","Approved")      #Changes the approved customer's detail from pending to approved
                    accept=open("RegisteredCustomer.txt", "a")     
                    accept.write(newline)       #Write the approved customer details into the approved customer file
                    accept.close()
                    register.truncate(0)        #Clears the registered customer details from the new customer file 
                    exitfileloop=True

                elif adminapproval==2:
                    newline=line.replace("ApprovalPending","Rejected")      #Changes the rejected customer's detail from pending to rejected
                    reject=open("RejectedCustomer.txt", "a")
                    reject.write(newline)       #Write the approved customer details into the rejected customer file
                    reject.close()
                    register.truncate(0)        #Clears the rejected customer details from the new customer file
                    exitfileloop=True

                else:
                    print("Incorrect Input")
                    continue
            
        print("You are done with processing approvals")
        if back()=="exit":      #Calls the back function to go back
            admin_f()
                    

#Function to let admin give unique loan IDs to already registered customer
def admin_f3():
    with open("RegisteredCustomer.txt", "r") as readfile:
        file=readfile.read()    #Reads the content into of the file into the variable

    with open("RegisteredCustomer.txt", "r") as readreg:
        for line in readreg:    
            readreglist=line.split()
            if readreglist[27]=="000000":   #Checks if the registered customer has already been given a loan ID or not
                import random
                newline=line.replace("000000",str(random.randint(99999,1000000)))   #If the registered customer doesn't have a loan ID the 000000 is replaced by a random loan ID
                newfile=file.replace(line,newline)      #The details with the new loan ID is replaced witht he details with no loan ID
                file=newfile
                with open("RegisteredCustomer.txt", "w") as regwrite:
                    regwrite.write(newfile)     #The whole file is written back with with 000000 changed to random loan IDs

    print("Loan IDs have been provided")
    if back()=="exit":
        admin_f()                  


#Function to let admin look for transactions with specific usernames
def admin_f4():
    with open("Transactions.txt","r") as admintrans:
        record=False
        admin_userid=input("Enter the username: ")      #Lets admin enter a username to check for transactions with specific username
        for line in admintrans:
            admintranslist=line.split()
            if admintranslist[1]==admin_userid:     #Looks for the username in the transactions file
                print(line)     #Displays the transaction details of the specific username
                record=True
                
    if record==False:       #To display when there is nothing else to diplay
        print("No such record exits")

    if back()=="exit":
        admin_f()


#Function to let admin look for transactions with specific loan types
def admin_f5():
    with open("Transactions.txt","r") as admintrans:
        record=False
        admin_ltype=input("Enter the loan type: ")      #Lets admin enter a loan type to check for transactions with specific loan type
        for line in admintrans:
            admintranslist=line.split()
            if admintranslist[7]==admin_ltype:      #Looks for the loan type in the transactions file
                print(line)     #Displays the transaction details of the specific loan type
                record=True

    if record==False:       #To display when there is nothing else to diplay
        print("No such record exits")

    if back()=="exit":
        admin_f()

    
#Function to let admin look for transactions with all usernames
def admin_f6():
    with open("Transactions.txt","r") as admintrans:
        for line in admintrans:
            admintranslist=line.split()
            print(line)

    if back()=="exit":
        admin_f()
    

#Function to let admin look for transactions with all loan types
def admin_f7():
    with open("Transactions.txt","r") as admintrans:
        for line in admintrans:
            admintranslist=line.split()
            print(line)

    if back()=="exit":
        admin_f()
            

#Function to display new customer functionalities to new customers
def nc():
    nc_exit=False
    while nc_exit==False:
        print("""
Your options are:
1. Check loan details
2. Use loan calculator to check loan amount
3. Register
4. Exit""")
    
        nc_function=int(input("What would you like to do?: "))

        if nc_function==1:
            nc_f1()
            
        elif nc_function==2:
            nc_f2()
            
        elif nc_function==3:
            nc_f3()
            
        elif nc_function==4:
            mainmenu()

        else:
            print("""
Incorrect input""")
            continue


#Function to display loan details for each type of loan
def nc_f1():
    nc_ltype_exit=False
    while nc_ltype_exit==False:
            print("""
1. Education Loan (EL)
2. Car Loan (CL)
3. Home Loan (HL)
4. Personal Loan (PL)
5. Exit""")
    
            nc_ltype=int(input("What type of loan would you like the details to?: "))
            if nc_ltype==1:
                with open("EducationLoan.txt", "r") as el:
                    el_read=el.read()
                    print(el_read)      #Displays the details of the loan from a text file containing the detials
                if back()=="exit":
                    continue
                
                    
            elif nc_ltype==2:
                with open("CarLoan.txt", "r") as cl:
                    cl_read=cl.read()
                    print(cl_read)
                if back()=="exit":
                    continue

            elif nc_ltype==3:
                with open("HomeLoan.txt", "r") as hl:
                    hl_read=hl.read()
                    print(hl_read)
                if back()=="exit":
                    continue

            elif nc_ltype==4:
                with open("PersonalLoan.txt", "r") as pl:
                    pl_read=pl.read()
                    print(pl_read)
                if back()=="exit":
                    continue

            elif nc_ltype==5:
                nc()

            else:
                print("""
Incorrect input""")
                continue


#Function to display loan calculator options for different types of loans
def nc_f2():
    nc_calc_exit=False
    while nc_calc_exit==False:
        print("""
1. Education Loan (EL)
2. Car Loan (CL)
3. Home Loan (HL)
4. Personal Loan (PL)
5. Exit""")

        nc_calc=int(input("Which loan type would you like a calculator for?: "))

        if nc_calc==1:
            nc_calc_el()
                    
        elif nc_calc==2:
            nc_calc_cl()
            
        elif nc_calc==3:
            nc_calc_hl()
            
        elif nc_calc==4:
            nc_calc_pl()
            
        elif nc_calc==5:
            nc()

        else:
            print("""
Incorrect input""")
            continue


#Function to let new customers regsiter to different types of loans
def nc_f3():  
    nc_ltype=input("Enter your loan type (EL/CL/HL/PL): ")
    while nc_ltype not in ["EL", "CL", "HL", "PL"]:     #Checks if the loan type entered by the username is incorrect and asks them to re-enter if it is
        print("Invalid Loan Type")
        nc_ltype=input("Enter your loan type (EL/CL/HL/PL): ")

    if nc_ltype=="EL":      #Calls different functions for different types of loan types to register for
        nc_reg_el()

    elif nc_ltype=="CL":
        nc_reg_cl()

    elif nc_ltype=="HL":
        nc_reg_hl()

    elif nc_ltype=="PL":
        nc_reg_pl()


#Function for a loan calculator for education loans
def nc_calc_el():
    nc_calc_amount=int(input("Enter your loan amount in RM: "))
    while nc_calc_amount>400000:    #If the loan amount requested by the customer is more than RM400,000 it asks them to re-enter
        print("Loan amount too high")
        nc_calc_amount=int(input("Enter your loan amount in RM: "))     
    nc_calc_tenure=int(input("Enter your loan duration in years: "))
    while nc_calc_tenure>30:        #If the loan duration requested by the customer is more than 30 years it asks them to re-enter
        print("Loan duration too long")
        nc_calc_tenure=int(input("Enter your loan duration in years: "))

    nc_calc_monthlytenure=nc_calc_tenure*12     #Calculate the loan details for the new customer
    nc_calc_amountfinal=nc_calc_amount/nc_calc_monthlytenure
    nc_calc_interest=(nc_calc_amount*1.75/100)/12
    nc_calc_amountpa=nc_calc_amountfinal+nc_calc_interest
    
    print("""Your interest rate is 1.75% p.a.
You will have to pay""", format(nc_calc_interest,".2f"), """in interest per month
The total amount will be""", format(nc_calc_amountpa,".2f"), "per month")

    if back()=="exit":
        nc_f2()


#Function for a loan calculator for car loans
def nc_calc_cl():
    nc_calc_salary=int(input("Enter your monthly salary in RM: "))
    if nc_calc_salary<2500:     #If the monthly salary is lower than RM2,500 the user is not permitted the loan so it exits out of the calculator
        print("Salary too low")
        if back()=="exit":
            nc_f2()

    nc_calc_amount=int(input("Enter your loan amount in RM: "))
    while nc_calc_amount>400000:    #If the loan amount requested by the customer is more than RM400,000 it asks them to re-enter
        print("Loan amount too high")
        nc_calc_amount=int(input("Enter your loan amount in RM: "))
    nc_calc_tenure=int(input("Enter your loan duration in years: "))
    while nc_calc_tenure>30:        #If the loan duration requested by the customer is more than 30 years it asks them to re-enter
        print("Loan duration too long")
        nc_calc_tenure=int(input("Enter your loan duration in years: "))

    nc_calc_monthlytenure=nc_calc_tenure*12     #Calculate the loan details for the new customer
    nc_calc_amountfinal=nc_calc_amount/nc_calc_monthlytenure
    nc_calc_interest=(nc_calc_amount*3.4/100)/12
    nc_calc_amountpa=nc_calc_amountfinal+nc_calc_interest

    print("""Your interest rate is 3.4% p.a
You will have to pay""", format(nc_calc_interest,".2f"), """in interest per month
The total amount will be""", format(nc_calc_amountpa,".2f"), "per month")

    if back()=="exit":
        nc_f2()


#Function for a loan calculator for home loans
def nc_calc_hl():
    nc_calc_salary=int(input("Enter your monthly salary in RM: "))
    nc_calc_amount=int(input("Enter your loan amount in RM: "))
    nc_calc_tenure=int(input("Enter your loan duration in years: "))
    while nc_calc_tenure>30:        #If the loan duration requested by the customer is more than 30 years it asks them to re-enter
        print("Loan duration too long")
        nc_calc_tenure=int(input("Enter your loan duration in years: "))
            
    nc_hl_exit=False
    while nc_hl_exit==False:
        
       
        nc_calc_monthlytenure=nc_calc_tenure*12     #Calculate the loan details for the new customer
        nc_calc_amountfinal=nc_calc_amount/nc_calc_monthlytenure
        nc_calc_interest=(nc_calc_amount*4/100)/12
        nc_calc_amountpa=nc_calc_amountfinal+nc_calc_interest

        print("""1. First Home
2. Second Home
3. Exit""")
        nc_hl_type=int(input("Enter your type of home: "))      #Asks the user if the loan is for their first home or second home
        
        if nc_hl_type==1:
            if nc_calc_amountpa>50/100*nc_calc_salary:      #If the monthly amount to pay is more than 50% of the customers monthly salary they can't get a loan for their first home
                print("The loan amount is too high for your salary")
                if back()=="exit":
                    nc_f2()

        elif nc_hl_type==2:  
            if nc_calc_amountpa>60/100*nc_calc_salary:      #If the monthly amount to pay is more than 60% of the customers monthly salary they can't get a loan for their second home
                print("The loan amount is too high for your salary")
                if back()=="exit":
                    nc_f2()

        elif nc_hl_type==3:
            nc_f2()

        else:
            print("Incorrect input")
            continue

        print("""Your interest rate is 4% p.a
You will have to pay""", format(nc_calc_interest,".2f"), """in interest per month
The total amount will be""", format(nc_calc_amountpa,".2f"), "per month")
        if back()=="exit":
            nc_f2()


#Function for a loan calculator for personal loans
def nc_calc_pl():
    nc_calc_salary=int(input("Enter your monthly salary in RM: "))
    if nc_calc_salary<2500:     #If the monthly salary is lower than RM2,500 the user is not permitted the loan so it exits out of the calculator
        print("Salary too low")
        if back()=="exit":
            nc_f2()

    nc_calc_amount=int(input("Enter your loan amount in RM: "))
    while nc_calc_amount>100000:    #If the loan amount requested by the customer is more than RM100,000 it asks them to re-enter
        print("Loan amount too high")
        nc_calc_amount=int(input("Enter your loan amount in RM: "))
    while nc_calc_amount<5000:      #If the loan amount requested by the customer is less than RM5,000 it asks them to re-enter
        print("Loan amount too low")
        nc_calc_amount=int(input("Enter your loan amount in RM: "))

    nc_calc_tenure=int(input("Enter your loan duration in years: "))
    while nc_calc_tenure>6:         #If the loan duration requested by the customer is more than 6 years it asks them to re-enter
        print("Loan duration too long")
        nc_calc_tenure=int(input("Enter your loan duration in years: "))
    while nc_calc_tenure<2:         #If the loan duration requested by the customer is less than 2 years it asks them to re-enter
        print("Loan duration too short")
        nc_calc_tenure=int(input("Enter your loan duration in years: "))


    if nc_calc_amount>=5000 and nc_calc_amount<=20000:      #Loan calculator for people that need loans between RM5,000 and RM20,000
        nc_calc_monthlytenure=nc_calc_tenure*12
        nc_calc_amountfinal=nc_calc_amount/nc_calc_monthlytenure
        nc_calc_interest=(nc_calc_amount*8/100)/12
        nc_calc_amountpa=nc_calc_amountfinal+nc_calc_interest
        print("""Your interest rate is 8% p.a
You will have to pay""", format(nc_calc_interest,".2f"), """in interest per month
The total amount will be""", format(nc_calc_amountpa,".2f"), "per month")

        if back()=="exit":
            nc_f2()

    elif nc_calc_amount>20000 and nc_calc_amount<=50000:    #Loan calculator for people that need loans between RM20,000 and RM50,000
        nc_calc_monthlytenure=nc_calc_tenure*12
        nc_calc_amountfinal=nc_calc_amount/nc_calc_monthlytenure
        nc_calc_interest=(nc_calc_amount*7/100)/12
        nc_calc_amountpa=nc_calc_amountfinal+nc_calc_interest
        print("""Your interest rate is 7% p.a
You will have to pay""", format(nc_calc_interest,".2f"), """in interest per month
The total amount will be""", format(nc_calc_amountpa,".2f"), "per month")

        if back()=="exit":
            nc_f2()

    if nc_calc_amount>50000 and nc_calc_amount<=100000:     #Loan calculator for people that need loans between RM50,000 and RM100,000
        nc_calc_monthlytenure=nc_calc_tenure*12
        nc_calc_amountfinal=nc_calc_amount/nc_calc_monthlytenure
        nc_calc_interest=(nc_calc_amount*6.5/100)/12
        nc_calc_amountpa=nc_calc_amountfinal+nc_calc_interest
        print("""Your interest rate is 6.5% p.a
You will have to pay""", format(nc_calc_interest,".2f"), """in interest per month
The total amount will be""", format(nc_calc_amountpa,".2f"), "per month")

        if back()=="exit":
            nc_f2()


#Function for education loan registeration
def nc_reg_el():
    nc_ltype="EL"
    nc_userid=username_check()  #Calls the unique username checking fucntion to let the user select a unique username

    nc_pw1=input("Enter your password: ")       #Lets user enter their password twice and make sure they match
    nc_pw2=input("Rewrite your password: ")
    while nc_pw1!=nc_pw2:
        print("The passwords don't match")
        nc_pw1=input("Enter your password: ")
        nc_pw2=input("Rewrite your password: ")

    if nc_pw1==nc_pw2:
        nc_confirmedpw=nc_pw1

    nc_name=input("Enter your name: ")      #Registration details for the user
    nc_address=input("Enter your address: ")
    nc_emailid=input("Enter your email id: ")
    nc_contactnumber=input("Enter your contact number: ")
    nc_gender=input("Enter your gender (Male, Female, Other): ")
    while nc_gender not in ["Male", "Female", "Other"]:     #Checks if the gender entered by the user is one of the options or not
        print("Invalid Gender")
        nc_gender=input("Enter your gender (Male, Female, Other): ")
    nc_dob=input("Enter your date of birth (DD/MM/YYYY): ")
    nc_reg_amount=int(input("Enter your loan amount in RM: "))
    while nc_reg_amount>400000:
        print("Loan amount too high")
        nc_reg_amount=int(input("Enter your loan amount in RM: "))
    nc_reg_tenure=int(input("Enter your loan duration in years: "))
    while nc_reg_tenure>30:
        print("Loan duration too long")
        nc_reg_tenure=int(input("Enter your loan duration in years: "))

    nc_reg_interest=nc_reg_amount*1.75/100
    nc_reg_totalamount=nc_reg_amount+nc_reg_interest
    nc_reg_mtenure=nc_reg_tenure*12
    nc_reg_mamount=nc_reg_totalamount/nc_reg_mtenure

    elreg=open("NewCustomer.txt", "a")     #Writes registered customer details into the new customer file
    elreg.write("Username: "+nc_userid+"\t"+"Password: "+nc_confirmedpw+"\t"+"Address: "+nc_address+"\t"+"EmailID: "+nc_emailid+"\t"+"ContactNumber: "+nc_contactnumber+"\t"+"Gender: "+nc_gender+"\t"+"DateOfBirth: "+nc_dob+"\t"+"LoanType: "+nc_ltype+"\t"+"AmountLoaned: "+str(format(nc_reg_amount,".2f"))+"\t"+"LoanDuration: "+str(nc_reg_tenure)+"\t"+"AmountLeftToPay: "+str(format(nc_reg_totalamount,".2f"))+"\t"+"MonthlyAmountToPay: "+str(format(nc_reg_mamount,".2f"))+"\t"+"MonthsLeftToPay: "+str(nc_reg_mtenure)+"\t"+"LoanID: "+"000000"+"\t"+"ApprovalStatus: "+"ApprovalPending"+"\n")
    elreg.close()
    print("Your account is registered, pending approval")
    nc()
    

#Function for car loan registeration
def nc_reg_cl():
    nc_ltype="CL"
    nc_userid=username_check()      #Calls the unique username checking fucntion to let the user select a unique username
    nc_pw1=input("Enter your password: ")       #Lets user enter their password twice and make sure they match
    nc_pw2=input("Rewrite your password: ")
    while nc_pw1!=nc_pw2:       
        print("The passwords don't match")
        nc_pw1=input("Enter your password: ")
        nc_pw2=input("Rewrite your password: ")

    if nc_pw1==nc_pw2:
        nc_confirmedpw=nc_pw1
    nc_name=input("Enter your name: ")
    nc_address=input("Enter your address: ")
    nc_emailid=input("Enter your email id: ")
    nc_contactnumber=input("Enter your contact number: ")
    nc_gender=input("Enter your gender (Male, Female, Other): ")
    while nc_gender not in ["Male", "Female", "Other"]:     #Checks if the gender entered by the user is one of the options or not
        print("Invalid Gender")
        nc_gender=input("Enter your gender (Male, Female, Other): ")
    nc_dob=input("Enter your date of birth (DD/MM/YYYY): ")
    nc_reg_salary=int(input("Enter your monthly salary in RM: "))
    if nc_reg_salary<2500:
        print("Your salary is too low")
        if back()=="exit":
            nc()
    nc_reg_amount=int(input("Enter your loan amount in RM: "))
    while nc_reg_amount>400000:
        print("Loan amount too high")
        nc_reg_amount=int(input("Enter your loan amount in RM: "))
    nc_reg_tenure=int(input("Enter your loan duration in years: "))
    while nc_reg_tenure>30:
        print("Loan duration too long")
        nc_reg_tenure=int(input("Enter your loan duration in years: "))

    nc_reg_interest=nc_reg_amount*3.4/100
    nc_reg_totalamount=nc_reg_amount+nc_reg_interest
    nc_reg_mtenure=nc_reg_tenure*12
    nc_reg_mamount=nc_reg_totalamount/nc_reg_mtenure

    clreg=open("NewCustomer.txt", "a")     #Writes registered customer details into the new customer file
    clreg.write("Username: "+nc_userid+"\t"+"Password: "+nc_confirmedpw+"\t"+"Address: "+nc_address+"\t"+"EmailID: "+nc_emailid+"\t"+"ContactNumber: "+nc_contactnumber+"\t"+"Gender: "+nc_gender+"\t"+"DateOfBirth: "+nc_dob+"\t"+"LoanType: "+nc_ltype+"\t"+"AmountLoaned: "+str(format(nc_reg_amount,".2f"))+"\t"+"LoanDuration: "+str(nc_reg_tenure)+"\t"+"AmountLeftToPay: "+str(format(nc_reg_totalamount,".2f"))+"\t"+"MonthlyAmountToPay: "+str(format(nc_reg_mamount,".2f"))+"\t"+"MonthsLeftToPay: "+str(nc_reg_mtenure)+"\t"+"LoanID: "+"000000"+"\t"+"ApprovalStatus: "+"ApprovalPending"+"\n")
    clreg.close()
    print("Your account is registered, pending approval")
    nc()


#Function for home loan registeration    
def nc_reg_hl():
    nc_ltype="HL"
    nc_userid=username_check()      #Calls the unique username checking fucntion to let the user select a unique username
            
    nc_pw1=input("Enter your password: ")       #Lets user enter their password twice and make sure they match
    nc_pw2=input("Rewrite your password: ")
    while nc_pw1!=nc_pw2:
        print("The passwords don't match")
        nc_pw1=input("Enter your password: ")
        nc_pw2=input("Rewrite your password: ")

    if nc_pw1==nc_pw2:
        nc_confirmedpw=nc_pw1
    nc_name=input("Enter your name: ")
    nc_address=input("Enter your address: ")
    nc_emailid=input("Enter your email id: ")
    nc_contactnumber=input("Enter your contact number: ")
    nc_gender=input("Enter your gender (Male, Female, Other): ")
    while nc_gender not in ["Male", "Female", "Other"]:     #Checks if the gender entered by the user is one of the options or not
        print("Invalid Gender")
        nc_gender=input("Enter your gender (Male, Female, Other): ")
    nc_dob=input("Enter your date of birth (DD/MM/YYYY): ")
    nc_reg_salary=int(input("Enter your monthly salary in RM: "))
    if nc_reg_salary<2500:
        print("Your salary is too low")
        if back()=="exit":
            nc()

    nc_reg_amount=int(input("Enter your loan amount in RM: "))
    while nc_reg_amount>400000:
        print("Loan amount too high")
        nc_reg_amount=int(input("Enter your loan amount in RM: "))
    nc_reg_tenure=int(input("Enter your loan duration in years: "))
    while nc_reg_tenure>30:
        print("Loan duration too long")
        nc_reg_tenure=int(input("Enter your loan duration in years: "))

    nc_reg_interest=nc_reg_amount*4/100
    nc_reg_totalamount=nc_reg_amount+nc_reg_interest
    nc_reg_mtenure=nc_reg_tenure*12
    nc_reg_mamount=nc_reg_totalamount/nc_reg_mtenure

    nc_reg_hltype_loop=True
    while nc_reg_hltype_loop==True:     #Loop to let user select their type of home
        print("""1. First Home
2. Second Home""")
        nc_reg_hltype=int(input("Enter your type of home: "))
        if nc_reg_hltype==1:
            if nc_reg_mamount>50/100*nc_reg_salary:     #Check if their salary is suitable for their loan amount
                print("The loan amount is too high for your salary")
                if back()=="exit":
                    nc()
            break

        elif nc_reg_hltype==2:
            if nc_reg_mamount>60/100*nc_reg_salary:
                print("The loan amount is too high for your salary: ")
                if back()=="exit":
                    nc()
            break

        else:
            print("Incorrect Input")
            continue
        
    hlreg=open("NewCustomer.txt", "a")     #Writes registered customer details into the new customer file
    hlreg.write("Username: "+nc_userid+"\t"+"Password: "+nc_confirmedpw+"\t"+"Address: "+nc_address+"\t"+"EmailID: "+nc_emailid+"\t"+"ContactNumber: "+nc_contactnumber+"\t"+"Gender: "+nc_gender+"\t"+"DateOfBirth: "+nc_dob+"\t"+"LoanType: "+nc_ltype+"\t"+"AmountLoaned: "+str(format(nc_reg_amount,".2f"))+"\t"+"LoanDuration: "+str(nc_reg_tenure)+"\t"+"AmountLeftToPay: "+str(format(nc_reg_totalamount,".2f"))+"\t"+"MonthlyAmountToPay: "+str(format(nc_reg_mamount,".2f"))+"\t"+"MonthsLeftToPay: "+str(nc_reg_mtenure)+"\t"+"LoanID: "+"000000"+"\t"+"ApprovalStatus: "+"ApprovalPending"+"\n")
    hlreg.close()
    print("Your account is registered, pending approval")
    nc()


#Function for home loan registeration
def nc_reg_pl():
    nc_ltype="PL"
    nc_userid=username_check()      #Calls the unique username checking fucntion to let the user select a unique username

    nc_pw1=input("Enter your password: ")       #Lets user enter their password twice and make sure they match
    nc_pw2=input("Rewrite your password: ")
    while nc_pw1!=nc_pw2:
        print("The passwords don't match")
        nc_pw1=input("Enter your password: ")
        nc_pw2=input("Rewrite your password: ")

    if nc_pw1==nc_pw2:
        nc_confirmedpw=nc_pw1
    nc_name=input("Enter your name: ")
    nc_address=input("Enter your address: ")
    nc_emailid=input("Enter your email id: ")
    nc_contactnumber=input("Enter your contact number: ")
    nc_gender=input("Enter your gender (Male, Female, Other): ")
    while nc_gender not in ["Male", "Female", "Other"]:     #Checks if the gender entered by the user is one of the options or not
        print("Invalid Gender")
        nc_gender=input("Enter your gender (Male, Female, Other): ")
    nc_dob=input("Enter your date of birth (DD/MM/YYYY): ")
    nc_reg_salary=int(input("Enter your monthly salary in RM: "))
    if nc_reg_salary<2500:
        print("Your salary is too low")
        if back()=="exit":
            nc()
    nc_reg_amount=int(input("Enter your loan amount in RM: "))
    while nc_reg_amount>100000:
        print("Loan amount too high")
        nc_reg_amount=int(input("Enter your loan amount in RM: "))
    while nc_reg_amount<5000:
        print("Loan amount too low")
        nc_reg_amount=int(input("Enter your loan amount in RM: "))
    nc_reg_tenure=int(input("Enter your loan duration in years: "))
    while nc_reg_tenure>6:
        print("Loan duration too long")
        nc_reg_tenure=int(input("Enter your loan duration in years: "))
    while nc_reg_tenure<2:
        print("Loan duration too short")
        nc_reg_tenure=int(input("Enter your loan duration in years: "))

    if nc_reg_amount>=5000 and nc_reg_amount<=20000:        #Checks which interest rate the loan amount requested belongs to
        nc_reg_interest=nc_reg_amount*8/100
        nc_reg_totalamount=nc_reg_amount+nc_reg_interest
        nc_reg_mtenure=nc_reg_tenure*12
        nc_reg_mamount=nc_reg_totalamount/nc_reg_mtenure

    elif nc_reg_amount>20000 and nc_reg_amount<=50000:
        nc_reg_interest=nc_reg_amount*7/100
        nc_reg_totalamount=nc_reg_amount+nc_reg_interest
        nc_reg_mtenure=nc_reg_tenure*12
        nc_reg_mamount=nc_reg_totalamount/nc_reg_mtenure

    elif nc_reg_amount>50000 and nc_reg_amount<=100000:
        nc_reg_interest=nc_reg_amount*6.5/100
        nc_reg_totalamount=nc_reg_amount+nc_reg_interest
        nc_reg_mtenure=nc_reg_tenure*12
        nc_reg_mamount=nc_reg_totalamount/nc_reg_mtenure

    plreg=open("NewCustomer.txt", "a")     #Writes registered customer details into the new customer file
    plreg.write("Username: "+nc_userid+"\t"+"Password: "+nc_confirmedpw+"\t"+"Address: "+nc_address+"\t"+"EmailID: "+nc_emailid+"\t"+"ContactNumber: "+nc_contactnumber+"\t"+"Gender: "+nc_gender+"\t"+"DateOfBirth: "+nc_dob+"\t"+"LoanType: "+nc_ltype+"\t"+"AmountLoaned: "+str(format(nc_reg_amount,".2f"))+"\t"+"LoanDuration: "+str(nc_reg_tenure)+"\t"+"AmountLeftToPay: "+str(format(nc_reg_totalamount,".2f"))+"\t"+"MonthlyAmountToPay: "+str(format(nc_reg_mamount,".2f"))+"\t"+"MonthsLeftToPay: "+str(nc_reg_mtenure)+"\t"+"LoanID: "+"000000"+"\t"+"ApprovalStatus: "+"ApprovalPending"+"\n")
    plreg.close()
    print("Your account is registered, pending approval")
    nc()


#Function to check if registered customer's request has been accepted, rejected or is still pending approval
def rc():
    account_exists=True
    while account_exists==True:
        with open("NewCustomer.txt", "r+") as pending, open("RegisteredCustomer.txt", "r") as approved, open("RejectedCustomer.txt", "r") as rejected:

            userid=input("Enter your username: ")
            password=input("Enter your password: ")
        
            for line1 in pending:
                pendinglist=line1.split()
                if userid==pendinglist[1] and password==pendinglist[3]:     #Checks if the username and password exists in the Pending Approval file
                    print("Your approval is pending")
                    if back()=="exit":
                        mainmenu()      #Takes them back to the main menu


            for line2 in approved:
                approvedlist=line2.split()
                if userid==approvedlist[1] and password==approvedlist[3]:   #Checks if the username and password exists in the Accepted Customer file
                    rc_f(userid, password)      #Lets them go to the registered customer functionalities with their username and password


            for line3 in rejected:
                rejectedlist=line3.split()
                if userid==rejectedlist[1] and password==rejectedlist[3]:   #Checks if the username and password exists in the Rejected Customer file
                    print("Your approval is rejected")
                    if back()=="exit":
                        mainmenu()      #Takes them back to the main menu
    
            print("Incorrect username or password")     #If the username and password is found in neither of the files then it might be incorrect
            rc_exit=input("Press any key to retry or 2 to exit: ")

            if rc_exit=="2":    #If user selects exit takes them back to main menu
                mainmenu()
            else:       #Otherwise restarts the loop
                continue


#Function to display a registered customer the registered customer functionalities
def rc_f(userid, password):
    rc_f_exit=False
    while rc_f_exit==False:
        print("""
Welcome Back""")

        print("""
Your options are:
1. Check loan detail 
2. Pay loan installment
3. View transactions
4. Check the status of loan
5. Exit""")

        rc_function=int(input("What would you like to do?: "))

        if rc_function==1:
            rc_f1(userid, password)

        elif rc_function==2:
            rc_f2(userid, password)

        elif rc_function==3:
            rc_f3(userid, password)

        elif rc_function==4:
            rc_f4(userid, password)

        elif rc_function==5:
            mainmenu()

        else:
            print("""
Incorrec Input""")
            continue


#Function to display the user's loan details
def rc_f1(userid, password):
    with open("RegisteredCustomer.txt","r") as details:
        for line in details:
            detaillist=line.split()
            if userid==detaillist[1] and password==detaillist[3]:   #Looks for the line with matching username and password and prints it
                print(line)

    if back()=="exit":
        rc_f(userid, password)


#Function to let the user pay their loan installment
def rc_f2(userid, password):
    with open("RegisteredCustomer.txt","r") as reg:
        rc_useridpay=userid     #Accepts payment detials from the customer
        rc_passwordpay=password
        rc_name=input("Enter your name: ")
        rc_creditcard=input("Enter your credit card number: ")
        rc_creditcardexpiry=input("Enter your credit card expiry date (DD/MM/YYYY): ")
        rc_creditcardsecurity=int(input("Enter your credit card secuiry number: "))
        rc_payment=float(input("Enter your exact payment amount: "))
        for linepay in reg:
            reglist=linepay.split()
            if rc_useridpay==reglist[1] and rc_passwordpay==reglist[3]:     #Finds the correct record of the user by mathing their username and passowrd
                rc_ltype=reglist[15]    
                rc_correctpayment=False
                while rc_correctpayment==False:     #Loops till the payment amount entered by the user is exact
                    
                    if str(rc_payment)==reglist[23]:

                        with open("RegisteredCustomer.txt","r") as reg2:
                            regwrite=reg2.read()
                                
                        changeamount=format((float(reglist[21])-rc_payment),".2f")      #Reduces the payment amount from the amount the user has to pay in total
                        changemonth=int(reglist[25])-1      #Reduces the number of months the user has to pay their loan for by 1
                        listtowrite=linepay.replace(reglist[21],str(changeamount))      #Replaces the new records with the old ones
                        listtowrite2=listtowrite.replace(reglist[25],str(changemonth))
                        regwrite=regwrite.replace(linepay, listtowrite2)

                        with open("RegisteredCustomer.txt","w") as reg3:
                            reg3.write(regwrite)    #Writes the new records back into the file

                        rc_correctpayment=True


                    else:
                        while str(rc_payment)!=reglist[23]:     
                            print("Your amount is either too low or too high")
                            rc_tran_exit=input("Press any key to retry or 2 to go back: ")
                            if rc_tran_exit=="2":   #If the user wants to exit it takes them back to the registered customer functionalities
                                rc_f(userid, password)
                            else:       #Otherwise it lets them try entering the exact amount that they need to pay
                                rc_payment=float(input("Enter your exact payment amount: "))
                        continue    #Restarts loop
                
                rc_pd=input("Enter your payment date (DD/MM/YYYY): ")       #Continues taking payment detials
                rc_address=input("Enter your address: ")
                print("Your payment has been successfully made")
                transactions=open("Transactions.txt","a")       #Writes all the transaction details into a file with all the transactions
                transactions.write("Username: "+rc_useridpay+"\t"+"Password: "+rc_passwordpay+"\t"+"Name: "+rc_name+"\t"+"LoanType: "+rc_ltype+"\t"+"CreditCard: "+rc_creditcard+"\t"+"AmountPaid: "+str(rc_payment)+"\t"+"PaymentDate: "+rc_pd+"\t"+"Address: "+rc_address+"\n")
                transactions.close()
                rc_f(userid,password)


#Function to display all the past transactions of the user
def rc_f3(userid, password):
    with open("Transactions.txt","r") as details:
        record=False
        for line in details:
            detaillist=line.split()
            if userid==detaillist[1] and password==detaillist[3]:   #Looks for the lines with the user's username and password and displays it
                print(line)
                record=True
        if record==True:
            pass
        else:       #To display when there is nothing else to display
            print("You have no recorded transactions")

    if back()=="exit":
        rc_f(userid, password)


#Function to display the the status of the user's loan
def rc_f4(userid, password):
    with open("RegisteredCustomer.txt","r") as details:
        for line in details:
            detaillist=line.split()
            if userid==detaillist[1] and password==detaillist[3]:
                if detaillist[25]=="0":     #If the months left to pay the loan for is 0
                    print("Your loan is completely paid for")
                else:       #Otherwise displays the monthls left to pay the loan for 
                    print("You have", detaillist[25],"months of loan to pay")

    if back()=="exit":
        rc_f(userid, password)


#Start
mainmenu()
