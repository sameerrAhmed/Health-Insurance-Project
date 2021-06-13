import pymysql

import datetime
#Connection Object
mydb = pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="insuranceDatabase")

#Cursor object
mycursor = mydb.cursor()
#============================


def callAdmin():
    print("---------Please Enter Login Details------------")
    Aid=int(input("Enter your Id: "))
    un=input("Enter Username:- ")
    pwd=input("Enter Password:- ")

    mycursor.execute("select * from AdminLoginTab where uName='{}' and pWord='{}'".format(un,pwd))
    AdminLoginTab=mycursor.fetchone()

    if AdminLoginTab:
        print("------------WELCOME {}-----------".format(AdminLoginTab[1]))

    else:
        print("INVALID Username or Password")

callAdmin()

def adminOptions():
    while True:
        print("1. POLICY DETAILS ENTRY")
        print("2. CUSTOMER LIST")
        print("3. POLICY TAKEN LIST")
        print("4. LOGOUT")

        ch=int(input("Enter Your Choice: "))

        if ch==1:
            pn=input("Enter Policy Name: ")
            pd=input("Enter Policy Details: ")
            instype=input("Enter Insurance Type: ")
            age=input("Enter Age Limit: ")
            maximumAmt=int(input("Maximum Amount: "))
            premAmt=int(input("Premium Amount: "))

            mycursor.execute("insert into InsDETtab(policyName,Details,insTypeNAme,AgeLimit,maxAmt,premiumAmt) values ('{}','{}','{}','{}',{},{})".format(pn,pd,instype,age,maximumAmt,premAmt))
            mydb.commit()
            print("=====POLICY DETAILS SUCCESSFULLY ENTERED=====")
            print()
            adminOptions()

        elif ch==2:
            un=input("Enter your username: ")
            pwd=input("Enter your password: ")
            name=input("Enter your name: ")
            addr=input("Enter your address: ")
            mobileNo=input("Enter your mobile number: ")
            email=input("Enter your email: ")
            qualific=input("Enter your qualification: ")
            designation=input("Enter your profession: ")

            mycursor.execute("insert into custdettab(uName,pWord,CustName,Caddr,MobileNo,email,qualification,designation) values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(un,pwd,name,addr,mobileNo,email,qualific,designation))
            mydb.commit()
            print("========CUSTOMER ADDED===========")
            print()
            adminOptions()
        
        elif ch==3:
            pNo=int(input("Enter Your Policy Number: "))
            CompName=(input("Enter Company Name: "))
            pDate=input("Enter date: ")
            userName=input("Enter Your Username: ")
            ApplicantName=input("Enter Your full name: ")
            addr=input("Enter Your Address: ")
            mobNo=int(input("Enter Your Mobile Num: "))
            email=input("Enter you Email: ")
            dob=input("Enter your DOB: ")
            gender=input("Gender (M/F/others): ")
            policyName=input("Enter Policy Name: ")
            policyAmt=int(input("Enter Policy Amount: "))
            policyduration=int(input("Enter Policy Duration in months: "))
            premiumAmt=int(input("Monthly Premium: "))

            mycursor.execute("insert into Policytab(PolicyNo,CompanyName,pDate,uName,AppName,appAdd,MobileNo,email,dob,gender,policyName,policyAmt,duration,premiumAmt) values ({},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},{},{})".format(pNo,CompName,pDate,userName,ApplicantName,addr,mobNo,email,dob,gender,policyName,policyAmt,policyduration,premiumAmt))
            mydb.commit()
            print("============POLICY TAKEN LIST HAS BEEN SUCCESSFULLY CREATED===============")
            print()
            adminOptions()

        elif ch==4:
            print("SUCCESSFULLY LOGOUT...")
            break
        
adminOptions()




