import webbrowser
from cart import add_to_cart
def kids():
    print("Kid's collection 👕👗\n")
    print("1.Frocks  \n"
      "2.T-shirts  \n"
      "3.Kurtas \n"
      "4.Jumpsuits \n")
    ch=int(input("Enter your choice from 1 to 4: \n"))
    if ch==1:
        webbrowser.open_new("https://www.amazon.in/Hopscotch-Cotton-Casual-Dresses-CDY-1457140/dp/B07P5N3DY8/ref=sr_1_8?crid=3KX6WCI8OIARI&dib=eyJ2IjoiMSJ9.dxv0ycD2Tv7FnylEEDXyFubVjUihZo3LB4ga019Hv15cpn908BtIDJ3kAeW94XZq_O64sFN_lkLLvSzeuXogUKemzTeJXCN7M3NCEgNpEoN-Dz1LP-u7hyAr2BXD5SDNceWaV12KWgTS7-nEu1HTIrGZVpMjUlRC9b0vsIasp5XNGf6qVEsddCIoiYHQySYBK1ux2curFBc0djSvDkAKJKQVpZjT_6Nd6sSXVnoLjlaQWFr49UtFnM3Tzc5wWqCtCo79LGg1AEEbOCUOfGsX4T_fGuyfkxFC-q1cc7sUknY.s7R4w6MCizxMJCURP9GBsOcLLzM8Nh_rOpaAeWMWSPs&dib_tag=se&keywords=kids%2Bfrock&qid=1750431798&sprefix=kids%2Bfrock%2Caps%2C353&sr=8-8&th=1&psc=1")
        print("Please check the price on the website before continuing!")
        price = 582
        qty = int(input("Enter quantity: "))
        add_to_cart("Frocks", price, qty)

    elif ch==2:
        webbrowser.open_new("https://www.flipkart.com/united-colors-benetton-boys-printed-pure-cotton-regular-t-shirt/p/itma652a3fc14c5a?pid=KTBHYGAHZMEY3BKZ&lid=LSTKTBHYGAHZMEY3BKZ8TF5BU&marketplace=FLIPKART&q=tshirt+for+kid&store=clo%2Fash%2Fank%2Fpgi&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=en_tcQXCEnrulKKzOa5Z9YhRrubdrp-6r3Qfmibd3vUSK4k6BkvwqmHqlpDIGRuG4_42JEG4W3ZdysAsRTBAKaPR_UFjCTyOHoHZs-Z5_PS_w0%3D&ppt=sp&ppn=sp&ssid=08hr506fr40000001750672024444&qH=069400605b834c26")
        print("Please check the price on the website before continuing!")
        price = 359
        qty = int(input("Enter quantity: "))
        add_to_cart("T-shirts", price, qty)
    elif ch==3:
        webbrowser.open_new("https://www.flipkart.com/md-enterprise-girls-wedding-kurta-palazzo-set/p/itm853c2c1cba42b?pid=KETGU2D2MPZFQQQU&lid=LSTKETGU2D2MPZFQQQUKOCNLY&marketplace=FLIPKART&q=kurtas+for+kid&store=clo%2Fcfv&srno=s_1_6&otracker=search&otracker1=search&fm=Search&iid=en_jwPGVQcbrhSXVh8s7mlezZAe7dvMSxpkFAPjGzMwL5_r2Xtn9d_wV7Cu7fwngAfAWgz6H0JUwZ9FpSkHf1Je2w%3D%3D&ppt=sp&ppn=sp&ssid=7vxwa1zp4w0000001750672056292&qH=1683f7bd91d48333")
        print("Please check the price on the website before continuing!")
        price = 439
        qty = int(input("Enter quantity: "))
        add_to_cart("Kurtas", price, qty)
    elif ch==4:
        webbrowser.open_new("https://www.flipkart.com/lm-fashion-striped-girls-jumpsuit/p/itmf561ad80f9177?pid=JUMHYQHZWWYTEYHH&lid=LSTJUMHYQHZWWYTEYHHENHINK&marketplace=FLIPKART&q=jumpsuit+for+girls+8+-+12+years&store=clo%2Fh4p%2F2z1%2F7zd&srno=s_1_21&otracker=AS_Query_OrganicAutoSuggest_5_5_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_5_5_na_na_ps&fm=search-autosuggest&iid=8193bc3b-d348-431a-9e69-70e70bae8db5.JUMHYQHZWWYTEYHH.SEARCH&ppt=sp&ppn=sp&ssid=u0xcwfrso00000001750672093070&qH=a426b39b8724f8fa")
        print("Please check the price on the website before continuing!")
        price = 238
        qty = int(input("Enter quantity: "))
        add_to_cart("Jumpsuits", price, qty)
    else:
        print("Invalid choice")
