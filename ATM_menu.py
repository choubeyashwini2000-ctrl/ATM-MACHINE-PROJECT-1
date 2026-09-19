from colorama import Fore,Style
import time
import random
print(Fore.YELLOW +"INSERT THE ATM CARD")
pin_a = 802119
n = int(input("enter 0 if inserted or 1 if not\n\t"))
atm = 0
Amount = 10000
def amount_withdraw():
    A = int(input("\tenter the amount to withdraw"))
    print(A,"\tamount u want to withdraw\n")
    
    i =0
    for i in range(3):
        pin = int(input("enter the pin of ur account\n\n"))
        if pin == pin_a:
            print(Fore.RED + "\tWITHDRAWAL SUCCESFULL\n")
            print(Amount - A, "\tur account have this much money\n")
            time.sleep(4)
            break   
            
        else:
            print("\tenter the correct pin\n\t")
            
def amount_deposite():
    d = int(input("\tenter the amount u want deposite\n"))
    i = 0
    for i in range(3):
        
        pin = int(input("enter the pin of ur account\n\n"))
        if pin == pin_a:
            
            print(Fore.WHITE + "deposite succesfull\n\nur account have :  ",Amount + d, "money\n\n\n\t")
            time.sleep(4)
            break
        else:
            print("\twrong pin\tenter new pin \n\t")
            
def amount_transfer():
    T = int(input("\tenter the amount that u want to transfer\n\t"))
    print(T,"the amount u want to transfer\n\t")
    ac = int(input("enter the account number IN WHICH U WNAT TO TRANSFER MONEY\n\t"))
    time.sleep(2)
    i = 0
    for i in range(3):
        pin = int(input("enter the pin of ur account\n\t"))
        if pin == pin_a:
            print(T,"amount transfer to : \t",ac,"\ndo u want to check amount now")
            
            
            print(Amount -T,"this amount is in ur account")
            time.sleep(3)
        else:
            print("\tenter the correct pin \t")
def change_pin():
    print(Fore.RED + "DO U WANT TO CHANGE PIN\n\t")
    i=0
    for i in range(3):
    
        pin = int(input("enter the pin of ur account\n\t"))
        if pin == pin_a:
            new_pin = int(input("\tenter the new pin\t\n"))    
            pia_a = new_pin
            print(pia_a, "\tis the new pin\n\t")
        else:
            print("\twrong pin \tenter correct one\t\n")
if (atm == 0):
    C = "check_balance"
    W = "withdraw"
    D = "Deposite"
    T = "Transfer"
    ch = "change_pin"
    # m = str(input("C = check balance\tW = withdraw\tD = Deposite\tT = Transfer\tch = change pin"))
    i =0
    while True:
        m = str(input("C = check balance\tW = withdraw\tD = Deposite\tT = Transfer\tch = change pin\n\t"))
        if m == "C":
            i = 0
            while True:
                pin = int(input("enter the pin of ur account\n"))
                if pin == pin_a:
                    time.sleep(2)
                    print(Fore.GREEN + "\tTHIS IS THE AMOUNT\t",Amount)
                    print("\tdo u want to withdraw\n")
                    m = int(input("\t1 for yes\t0 for no\n\t"))
                    if(m==1):
                        print("\tlets go\n\t")
                        amount_withdraw()
                        break
                        
                
                    else:
                        print("B")
                        break
                else:
                    print("wrong pin \tenter correct\n\t\t")
                    break
        
            
        elif m == "W":
            r = int(input("\tamount u want to withdraw\n\t"))
            print(r,"\tamount u want to withdraw\n")
            i =0
            for i in range(3):
                pin = int(input("enter the pin of ur account\n"))
                if pin == pin_a:
                    print(Fore.RED + "\tWITHDRAWAL SUCCESFULL\n")
                    print(Amount - r, "\tur account have this much money\n")
                    
                    break
                
        elif m == "D":
            amount_deposite()
            
        elif m == "T":
            amount_transfer()
            
        elif m == "ch":
            change_pin()
            
        else:
            print("wrong demand\t\nenter correct demand\n\t")
elif atm == 1:
    print(Fore.GREEN + "\n\twhy are u here then\tgo to hell\n\tRemove our card and run towands ur home fast and first...   BYE BYE")