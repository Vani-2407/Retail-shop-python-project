from  payment import  animation
from payment import sound
from  payment import  payment_gateway
from cart import show_cart
print(" Welcome to Retail therapy 🛍!!!!!!")
name=str(input("Enter your name:"))
ph=int(input("Enter your mobile number:"))
while True:
    print("In which section would you like to shop?\n"
      "1.Men\n"
      "2.Women\n"
      "3.Kids\n"
      "4.Exit and show the bill")
    ch=int(input("Enter the choice from 1 to 4:"))
    if ch==1:
        import men
        men.mens()
    elif ch==2:
        import women
        women.womens()
    elif ch==3:
        import kid
        kid.kids()
    elif ch==4:
        success = payment_gateway()
        if success:
            show_cart(name, ph)
        else:
            print("⚠️ Payment failed or cancelled. Bill not shown.")
        break
    else:
        print("Invalid choice please try again later")

        

    
    
