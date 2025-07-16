import webbrowser
from cart import add_to_cart
def mens():
    print("Men's collection 👔 \n")
    print("1.T-shirt  \n"
      "2.Pants  \n"
      "3.Formals  \n"
      "4.Shorts  \n")
    ch=int(input("Enter your choice from 1 to 4: \n"))
    if ch==1:
        webbrowser.open_new("https://www.flipkart.com/force-solid-men-round-neck-beige-t-shirt/p/itm29d3f6369ed0c")
        print("Please check the price on the website before continuing!")
        price = 256
        qty = int(input("Enter quantity: "))
        add_to_cart("T-shirt", price, qty)
    elif ch==2:
        webbrowser.open_new("https://www.flipkart.com/dennis-lingo-slim-fit-men-green-trousers/p/itmaf18a877d23cc?pid=TROGUHFFVNBM8U43&lid=LSTTROGUHFFVNBM8U43CE6S8E&marketplace=FLIPKART&q=pants+for+men&store=clo%2Fvua&srno=s_5_186&otracker=search&otracker1=search&fm=Search&iid=b38ef2d8-790a-456a-baf0-5eca37316592.TROGUHFFVNBM8U43.SEARCH&ppt=sp&ppn=sp&ssid=1r69s85geo0000001750689587520&qH=913b656f7a5d4415")
        print("Please check the price on the website before continuing!")
        price = 810
        qty = int(input("Enter quantity: "))
        add_to_cart("Pants", price, qty)  
    elif ch==3:
        webbrowser.open_new("https://www.flipkart.com/luqatti-men-solid-formal-green-shirt/p/itm12d0f8583c555?pid=SHTGGSM5SFYANFTF&lid=LSTSHTGGSM5SFYANFTFW4NECO&marketplace=FLIPKART&q=olive+green+formal+shirt++for+men+for+600&store=clo%2Fash%2Faxc%2Fmmk&srno=s_1_7&otracker=search&otracker1=search&fm=Search&iid=49cd5d90-862e-48b3-96f2-beb504cfae25.SHTGGSM5SFYANFTF.SEARCH&ppt=sp&ppn=sp&ssid=fxrhpcgwc00000001750689813648&qH=057ab32e2c00b9fb")
        print("Please check the price on the website before continuing!")
        price = 439
        qty = int(input("Enter quantity: "))
        add_to_cart("Formals", price, qty)    
    elif ch==4:
        webbrowser.open_new("https://www.flipkart.com/torontocn-solid-men-green-cargo-shorts/p/itm50e88db23cd14?pid=SRTHAQ37WQBSXHCT&lid=LSTSRTHAQ37WQBSXHCTCVJHZF&marketplace=FLIPKART&q=shorts+for+men&store=clo%2Fvua%2Fe8g%2Fkc7&srno=s_1_19&otracker=search&otracker1=search&fm=Search&iid=6ec75051-88ec-4ff6-b479-cebe96b632a7.SRTHAQ37WQBSXHCT.SEARCH&ppt=sp&ppn=sp&ssid=hapytak5r40000001750689972300&qH=187520f21506040b")
        print("Please check the price on the website before continuing!")
        price = 461
        qty = int(input("Enter quantity: "))
        add_to_cart("Shorts", price, qty)  
    else:
        print("Invalid choice")

