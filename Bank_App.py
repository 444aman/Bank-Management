import sys
import random
import fileinput
import base64
import time







def interest():
    f=open("Data.txt",'r')
    global fin_bal
    interest_rate=1
    temp='acc:'
    for i in f.readlines():
        if i.startswith(temp+str(ope_acc)):
            a = i.split()
            b = dict(map(str, x.split(':')) for x in a)
            cur=b['time']
            cur=float(cur)
            now=time.time()
            
            diff=now-cur
            days = diff //(60*60*24)
            
            interest_rate = float(interest_rate)/float(30) * days
            
            fin_bal=(int(b['balance'])/100) * interest_rate
            
            f.flush()
            f.close()
            
    
    


def blank_lines():
    
    if count == 1:
        Lines1=open("Data.txt").readlines()
        Lines=[x for x in Lines1 if x.strip()]
        open("Data.txt","w").writelines(Lines)
        raw_input("Press Enter To Return TO Main menu")
        main()
    else:
        old_pwd()





def intro():
    print '=' * 30
    print 'Bank \n Management \n System'
    print '=' * 30

    print 'BY SADHWANI AMAN '
    raw_input(" ")
    main()
    


def validate_mobile():
    if count == 1:
        while True:
            global number
            number = raw_input('Enter 10 Digit  Mobile Number: ')
            if 9 < len(number) < 11:
                break
            else:
                print "Enter Valid 10 Digit Mobile Number "
    else:
        old_pwd()


def validate_account():
    global acc
    check = False
    while check == False:

        acc = random.randint(100, 200)

        file1 = open('account.txt', 'a')
        file1.close()

        file1 = open("account.txt", 'r')
        data = file1.read()
        data = data.split('\n')
        data.pop()
        data = map(int, data)

        if acc in data:
            print 'trying again'
        else:
            file1 = open("account.txt", 'a')
            temp = str(acc)
            file1.write(temp + "\n")
            file1.close()
            check = True


def validate_balance():
    if count == 1:
        global dep_amt

        while True:
            try:
                dep_amt = int(raw_input("Enter Opening Balance Amount: "))
                return False
            except ValueError:
                print "Please Integer Values Only "
    else:
        old_pwd()


def write_data():
    fin = open("Data.txt", "a")
    fin.write('\n')
    fin.write("acc:")
    fin.write(str(acc))
    fin.write(" name:")
    fin.write(name)
    fin.write(" city:")
    fin.write(city)
    fin.write(" number:")
    fin.write(str(number))
    fin.write(" balance:")
    fin.write(str(dep_amt))
    fin.write(" time:")
    fin.write(str(time.time()))

    print '-' * 15
    print 'Account Number :', acc

    print 'New Account SuccessFully Created ....'
    print '-' * 15
    
    
    fin.close()
    blank_lines()
    raw_input("Press Enter To Return To Main Menu")
    main()

    


def write_account():
    
    if count == 1:
        print '-*' * 20
        print '\n New Account \n'
        print '-*' * 20

        global name, dep_amt, city
        name = raw_input("Enter Customer  Name :")
        city = raw_input("Enter Customer City :")
        validate_mobile()
        
        validate_account()
        
        validate_balance()
        
        write_data()
    else:
        old_pwd()


def deposit_money():
    if count == 1:
    
        while True:
            f = open("account.txt", 'r')
            data = f.read()
            data = data.split()
            global ope_acc
            f.close()

            try:
                ope_acc = int(raw_input('Enter Account Number :'))
                interest()
                temp = 'acc:'

                if str(ope_acc) in data:
                    with open("Data.txt", 'r') as f:
                        for i in f.readlines():
                            if i.startswith(temp + str(ope_acc)):
                                a = i.split()
                                b = dict(map(str, x.split(':')) for x in a)
                                c = int(b['balance'])+int(fin_bal)
                                d = int(c)
                                print "Current Balance :", d
                                name = b['name']
                                city = b['city']
                                number = b['number']
                                dep_amt = int(raw_input('Enter Amount To Deposit :'))
                                dep_amt += d

                                b['balance'] = str(dep_amt)
                                f.flush()

                                with open("Data.txt", "r") as f1:
                                    lines = [x for x in f1.readlines() if not x.startswith(temp + str(ope_acc))]
                                    f1.flush()

                                with open("Data.txt", "r") as f3:
                                    lines1 = [x for x in f3.readlines() if x.startswith(temp + str(ope_acc))]
                                    f3.flush()

                                with open("Data.txt", "w") as f2:
                                    f2.writelines(lines)
                                    f2.flush()
                                with open("Data.txt", "a") as fin:
                                    fin.write('\n')
                                    fin.write(temp + str(ope_acc))
                                    fin.write(" name:")
                                    fin.write(name)
                                    fin.write(" city:")
                                    fin.write(city)
                                    fin.write(" number:")
                                    fin.write(number)
                                    fin.write(" balance:")
                                    fin.write(str(dep_amt))
                                    fin.write(" time:")
                                    fin.write(str(time.time()))
                                    fin.flush()
                                    print '-' * 55
                                    print "Amount SuccessFully Deposited New Balance is :", dep_amt
                                    print '-' * 55
                                    blank_lines()
                                    raw_input("Press Enter To Resturn To Main Menu")
                                    main()
                                return True
            except ValueError:
                print "Please Enter Integer Values Only "
            else:
                print 'Please Enter Valid Account Number'
    else:
        old_pwd()


def withdraw_money():
    if count == 1:
    
        while True:
            f = open("account.txt", 'r')
            data = f.read()
            data = data.split()
            f.close()
            temp = 'acc:'
            global ope_acc
            try:
                ope_acc = int(raw_input("Enter Account Number "))
                interest()
                if str(ope_acc) in data:
                    with open("Data.txt", 'r') as f1:
                        lines = [x for x in f1.readlines() if not x.startswith(temp + str(ope_acc))]
                        f1.flush()
                    with open("Data.txt", 'r') as f2:
                        lines1 = [x for x in f2.readlines() if x.startswith(temp + str(ope_acc))]
                        f2.flush()
                    with open("Data.txt", 'r') as f3:
                        for i in f3.readlines():
                            if i.startswith(temp + str(ope_acc)):
                                a = i.split()
                                b = dict(map(str, x.split(':')) for x in a)
                                c = int(b['balance']) +  int(fin_bal)
                                name = b['name']
                                city = b['city']
                                number = b['number']
                                balance = int(c)
                                print 'Current Balance is :', balance
                                f3.flush()

                        wid_amt = int(raw_input("Enter Amount To Withdraw :"))
                        if wid_amt < balance:
                            balance -= wid_amt

                            with open("Data.txt", "w") as f4:
                                f4.write("\n")
                                f4.writelines(lines)
                                f4.flush()
                            with open("Data.txt", 'a') as f5:
                                f5.write("\n")
                                f5.write(temp + str(ope_acc))
                                f5.write(" name:")
                                f5.write(name)
                                f5.write(" city:")
                                f5.write(city)
                                f5.write(" number:")
                                f5.write(number)
                                f5.write(" balance:")
                                f5.write(str(balance))
                                f5.write(" time:")
                                f5.write(str(time.time()))
                                f5.flush()
                                print '-' * 55
                                print 'Amount SuccessFully Withdraw New Balance is :', balance
                                print '-' * 55
                                blank_lines()
                                raw_input("Press Enter To Resturn To Main Menu")
                                main()
                                return True

                        else:
                            print 'Cannot Withdraw Insufficient balance'
                            continue

            except ValueError:
                print 'Please Enter Integer Values Only '
            else:
                print 'Please Enter Valid Account Number.....'
    else:
        old_pwd()


def display_balance():
    if count == 1:
        f = open("account.txt", 'r')
        data = f.read()
        data = data.split()
        data.sort()
        f.close()
        global ope_acc
        while True:
            try:
                ope_acc = int(raw_input('Enter Account Number :'))
                interest()
                if str(ope_acc) in data:
                    f = open('Data.txt', 'r')
                    temp = "acc:"
                    for i in f.readlines():
                        if i.startswith(temp + str(ope_acc)):
                            a = i.split()
                            b = dict(map(str, x.split(':')) for x in a)
                            print '-' * 25
                            print 'Account No :', ope_acc
                            print 'Balance :', int(b['balance']) + int(fin_bal)
                            print '-' * 25
                            f.close()
                            raw_input("Press Enter To Resturn To Main Menu")
                            main()

                            return False
                else:
                    print 'acc not avail'
            except ValueError:
                print 'Please Enter Integer Values Only '
    else:
        old_pwd()


def display_all():
    if count == 1:
        f = open("account.txt", 'r')
        data = f.read()
        data = data.split()
        data.sort()
        f.close()
        global ope_acc
        while True:
            try:
                ope_acc = int(raw_input('Enter Account Number :'))
                interest()
                if str(ope_acc) in data:
                    f = open('Data.txt', 'r')
                    temp = 'acc:'
                    for i in f.readlines():
                        if i.startswith(temp + str(ope_acc)):
                            a = i.split()
                            b = dict(map(str, x.split(':')) for x in a)
                            print '-' * 25
                            print 'Account No :', ope_acc
                            print 'Name :', b['name']
                            print 'City :', b['city']
                            print "Mobile no :", b['number']
                            print 'Balance :', int(b['balance']) + int(fin_bal)
                            print '-' * 25
                            f.close()
                            raw_input("Press Enter To Resturn To Main Menu")
                            main()

                            return False
                else:
                    print 'acc not avail'
            except ValueError:
                print 'Please Enter Integer Values Only '
    else:
        old_pwd()



def delete_account():
    
    if count == 1:
        while True:
            a = open("account.txt", 'r')
            data = a.read()
            data=data.split()
            a.close()
            
            try:
                del_acc = int(raw_input("enter account number to delete :"))
                temp = 'acc:'
                if str(del_acc) in data:
                    with open("Data.txt", "r") as f1:
                        lines = [x for x in f1.readlines() if not x.startswith(temp + str(del_acc))]
                        f1.flush()
                        
                    with open("Data.txt", "w") as f2:
                        f2.writelines(lines)
                        f2.flush()
                        
                    with open("account.txt", "r") as f3:
                        lines = [x for x in f3.readlines() if not x.startswith(str(del_acc))]
                        f3.flush()
                        
                    with open("account.txt", "w") as f4:
                        f4.writelines(lines)
                        f4.flush()
                        
                    

                    print 'Account number: ', del_acc, ' Has been Deleted'
                    raw_input("Press Enter To Resturn To Main Menu")
                    main()

                    return True
                else:
                    print 'account not available'
            except ValueError:
                print 'Please Enter Integer Values Only '
    else:
        old_pwd()



def edit_account(): 
    if count == 1:
        f = open("account.txt", 'r')
        data = f.read()
        data = data.split('\n')

        
        f.close()
        global ope_acc
        while True:
            try:
                ope_acc = int(raw_input("enter acc no :"))
                interest()
                temp = 'acc:'
                if str(ope_acc) in data:

                    with open("Data.txt", "r") as f1:
                        lines = [x for x in f1.readlines() if not x.startswith(temp + str(ope_acc))]
                        f1.flush()

                    with open("Data.txt", "r") as f3:
                        lines1 = [x for x in f3.readlines() if x.startswith(temp + str(ope_acc))]
                        f3.flush()

                    with open("Data.txt", 'r') as f:
                        for i in f.readlines():
                            if i.startswith(temp + str(ope_acc)):

                                a = i.split()
                                b = dict(map(str, x.split(':')) for x in a)
                                print '-' * 20
                                print "OLD DETAILS :"
                                print "Name :", b['name']
                                print "City :", b['city']
                                print "Number :", b['number']
                                print 'Balance :', int(b['balance']) + int(fin_bal)
                                print '-' * 20
                                print 'Enter New Details'

                                city = raw_input("Enter City :")
                                validate_mobile()

                                b['acc'] = str(ope_acc)
                                name=b['name']
                                b['city'] = city
                                b['number'] = number
                                dep_amt=b['balance']
                                f.flush()


                                with open("Data.txt", "w") as f2:
                                    f2.writelines(lines)
                                    f2.flush()
                                with open("Data.txt", "a") as fin:
                                    fin.write('\n')
                                    fin.write(temp + str(ope_acc))
                                    fin.write(" name:")
                                    fin.write(name)
                                    fin.write(" city:")
                                    fin.write(city)
                                    fin.write(" number:")
                                    fin.write(number)
                                    fin.write(" balance:")
                                    fin.write(str(dep_amt))
                                    fin.write(" time:")
                                    fin.write(str(time.time()))
                                    fin.flush()
                                print '-' * 20
                                print 'new details for Account No :',ope_acc
                                print '-' * 20
                                print "Name :", b['name']
                                print "City :", b['city']
                                print "Number :", b['number']
                                print "Balance :", b['balance']
                                print '-' * 20
                                print 'Updated Successfully......'
                                blank_lines()
                                
                                raw_input("Press Enter To Resturn To Main Menu")
                                main()

                                return False
                else:
                    print 'Account No Avail'
            except ValueError:
                print 'Please Enter Integer Values Only '
    else:
        old_pwd()


def change_pwd():
    try:
      f = open("pass.txt", "r")
      data=f.read()
      data=data.split()
      temp=data[0]
      temp=base64.decodestring(temp)
      
      f.close()
      pwd=raw_input("Enter Your Current Password :")
      if pwd == temp:
          new_pwd()
      else:
          print 'Current Password Is Incorrect'
          print 'You Are Logged Out...'
      
    except IOError:
        print 'file err'



global count
count = 0


def main():
    
    
    
    if count == 1:
        
    
        print '*' * 30
        print 'Welcome to Banking Application'
        print '*' * 30

        print "\n\n\n\t MAIN MENU"
        print "\n\n\n\t 01. NEW ACCOUNT"
        print "\n\n\t02. DEPOSIT AMOUNT"
        print "\n\n\t03. WITHDRAW AMOUNT"
        print "\n\n\t04. BALANCE ENQUIRY"
        print "\n\n\t05. CUSTOMER DETAIL"
        print "\n\n\t06. DELETE AN ACCOUNT"
        print "\n\n\t07. MODIFY AN ACCOUNT"
        print "\n\n\t08 Change PASSWORD"
        print "\n\n\t09 REMOVE BLANK LINES"
        print "\n\n\t10. EXIT"
        print "\n\n\tSelect Your Option (1-8) "

        while True:
            try:
                choice = int(raw_input("Enter Your Choice :"))
                if choice == 1:
                    write_account()
                    break
                elif choice == 2:
                    deposit_money()
                    break
                elif choice == 3:
                    withdraw_money()
                    break
                elif choice == 4:
                    display_balance()
                    break
                elif choice == 5:
                    display_all()
                    break
                elif choice == 6:
                    delete_account()
                    break
                elif choice == 7:
                    edit_account()
                    break
                elif choice == 8:
                    change_pwd()
                    break
                elif choice == 9:
                    blank_lines()
                    break
                elif choice == 10:
                    sys.exit('Bye')
                else:
                    print 'Enter Valid Choice'
            except ValueError:
                print "Please Integer Values Only "
    else:
        old_pwd()


def new_pwd():
   f=open("pass.txt",'w')
   print '-' * 20
   pwd=raw_input("Enter New Password :")
   con=raw_input("Re-Enter New Password :")
   if pwd == con :
       f1=open('Data.txt','a')
       
       f1.close()
       f2=open('account.txt','a')
       
       f2.close()
       c=base64.encodestring(pwd)
       f.write(c)
       print 'new password set successfully..'
       print 'Please Re-Login '
       print '-' * 20
   else:
      print 'Password Dont Match'
      new_pwd()
   f.close()






def old_pwd():
    global count
    
    
    try:
        
      
      f = open("pass.txt", "r")
      data=f.read()
      data=data.split()
      temp=data[0]
      temp=base64.decodestring(temp)
      print '-' * 20
      pwd=raw_input("Enter Your Password :")
      if pwd == temp:
          f1=open('Data.txt','a')
          
          f1.close()
          f2=open('account.txt','a')
          
          f2.close()
          count+=1
          intro()
          
          


      else:
          print 'Incorrect Password '

    except IOError:
      new_pwd()




old_pwd()









