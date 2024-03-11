def ATM():
    username=['sruthi','pallavi','raj','bijoy']
    password=['sruthi12','pallavi12','raj12','bijoy12']
    pin=[1242,1233,1232,4546]
    balance=[234567,133456,35365,343545,2334445]
    print("enter your username")
    user=input()
    n=3
    if user in username:
        i=username.index(user)
        pass_word=input("password:")
        while n>0:
            if pass_word==password[i]:
                print("1.withdraw")
                print("2.deposit")
                print("3.balance")
                print("4.change password")
                print("5.logout")
                choice=int(input("enter your choice from 1-5:"))
                if choice==1:
                    print("enter amount to withdraw,remember that withdrawal amount should be lesser than balance amount")
                    amount=int(input())
                    print("enter your pin:")
                    unique_pin=int(input())
                    if unique_pin==pin[i]:
                        if amount<=balance[i]:
                            balance[i]-=amount
                            print("collect your cash")
                            print("do you want to display your balance")
                            print("1.yes")
                            print("2.no")
                            option=int(input())
                            if option==1:
                                print(balance[i])
                                print("would you like to exit")
                                print("1.yes")
                                print("2.no")
                                c=int(input())
                                if c==1:
                                    print("Thankyou!")
                                    break
        
                                else:
                                    pass
                                
                            else:
                                print("would you like to exit")
                                print("1.yes")
                                print("2.no")
                                c=int(input())
                                if c==1:
                                    print("Thankyou!")
                                    break
        
                                else:
                                    pass
                                
                        else:
                            print("your withdrawal amount is more than current balance")
                    else:
                        print("wrong pin")
                        break
                elif choice==2:
                    print("enter your pin:")
                    unique_pin=int(input())
                    if unique_pin==pin[i]:
                        print("enter amount to deposit")
                        cash=int(input())
                        balance[i]+=cash
                        print("you have deposited your money succesfully")
                        print("do you want to display your balance")
                        print("1.yes")
                        print("2.no")
                        o=int(input())
                        if o==1:
                            print(balance[i])
                            print("would you like to exit")
                            print("1.yes")
                            print("2.no")
                            c=int(input())
                            if c==1:
                                print("Thankyou!")
                                break
        
                            else:
                                pass
                            
                        else:
                            print("would you like to exit")
                            print("1.yes")
                            print("2.no")
                            c=int(input())
                            if c==1:
                                print("Thankyou!")
                                break
        
                            else:
                                pass
                             
                            
                    else:
                        print("you entered wrong pin")
                        break
                            
                elif choice==3:
                    print("enter your pin:")
                    unique_pin=int(input())
                    if unique_pin==pin[i]:
                        print("your current balance is",balance[i])
                        print("would you like to exit")
                        print("1.yes")
                        print("2.no")
                        c=int(input())
                        if c==1:
                            print("Thankyou!")
                            break
        
                        else:
                            pass
                        
                    else:
                        print("you entered wrong pin")
                        break
                
                    
                elif choice==4:
                    print("enter your pin:")
                    unique_pin=int(input())
                    if unique_pin==pin[i]:
                        print("password should contain minimum 8 characters,atleast one special character,atleast one uppercase,atleast one lowercase and atleast one digit")
                        print("enter new password:")
                        new_password=input()
                        print("confirm password:")
                        confirm_password=input()
                        if new_password==confirm_password:
                            if password[i]!=new_password:
                                if len(new_password) >= 8 and any(m.isupper() for m in new_password) and any(m.islower() for m in new_password) and any(m.isdigit() for m in new_password) and any(not m.isalnum() for m in new_password):
                                        print("password is succesfully updated")
                                        print("would you like to exit")
                                        print("1.yes")
                                        print("2.no")
                                        c=int(input())
                                        if c==1:
                                           print("Thankyou!")
                                           break
        
                                        else:
                                           pass
                                        
                                else:
                                        print("your password isnot strong enough")
                                        
                            else:
                        
                                 print("new_Password and confirm_password shouldnot match")
                        else:
                            print("your current password and new password are same")
                            break
                    else:
                        print("you entered wrong pin")
                        break
                elif choice==5:
                    print("confirm,if you want to logout")
                    print("1.yes")
                    print("2.n0")
                    b=int(input())
                    if b==1:

                        print("loggedout succesfully")
                        break
                    else:
                        pass
                else:
                    print("there is no such an option")
            else:
                n-=1
                if n>0:
                    print("incorect password",n,"attempts left")
                    pass_word=input()
                    
                else:
                   print("incorect password,account blocked")
                   break