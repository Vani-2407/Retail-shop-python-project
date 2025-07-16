import webbrowser
from cart import add_to_cart
def womens():
    print("Women's collection 🥻\n")
    print("1.Sarees  \n"
      "2.Pants  \n"
      "3.Kurtas \n"
      "4.T-shirts  \n")
    ch=int(input("Enter your choice from 1 to 4: \n"))
    if ch==1:
        webbrowser.open_new("https://www.flipkart.com/yashika-printed-daily-wear-art-silk-saree/p/itm91e80f44393a8?pid=SARGXZHGJGFZF5HC&lid=LSTSARGXZHGJGFZF5HCIHUKKS&marketplace=FLIPKART&store=clo%2F8on%2Fzpd%2F9og&srno=b_1_24&otracker=browse&fm=search-autosuggest&iid=64c5cec6-c5a3-4b9b-9060-e820d45cf2da.SARGXZHGJGFZF5HC.SEARCH&ppt=browse&ppn=browse&ssid=rjnu0lqlog0000001750430028765")
        print("Please check the price on the website before continuing!")
        price = 269
        qty = int(input("Enter quantity: "))
        add_to_cart("Sarees", price, qty)

    elif ch==2:
        webbrowser.open_new("https://www.amazon.in/Symbol-Premium-Relaxed-Business-SBP-SS24-WTR-710_Beige_40/dp/B0CSFPF5P6/ref=sr_1_1_sspa?crid=3IQ2SYDRC1OK1&dib=eyJ2IjoiMSJ9.AET1TNBCgarT8tGlndhVVZlkRdVbi7d-iNAIg9Fg9xA6m8_BcIOE0ffMSrxAPaYNKfwz42N8mM7sZCsTnY7BkR-Y15IwzV_PvM1Ig-bwRf1Xk8MyjGeWEfVlu5aBc4P_SvwFPuiqEFPPd7HrAztiVC8HN8_Eave3PZLB7vOTl8AkifsGiAiTGlihoVfkFm4_bW5r1CWcTJPJbT_bJ9XDwG_oYyrz7Xk6WCOCvhI2a4zdIMY1QrJxmu5FsB85wBFk8Qi1W7U5NNuLnPSCcsRypFZWgFK0M18opAeZ3Ex2lG0.kCkYveLuRQJWt7B0Ie6Voqv6X3MHUbwT6094bgEvULI&dib_tag=se&keywords=women%2Bpants&qid=1750670122&sprefix=women%2Bpant%2Caps%2C1073&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&psc=1")
        print("Please check the price on the website before continuing!")
        price = 1649
        qty = int(input("Enter quantity: "))
        add_to_cart("Pants", price, qty)
    elif ch==3:
        webbrowser.open_new("https://www.amazon.in/INDO-ERA-Straight-Embroidered-KH9MT7107_Small/dp/B0C7R8RZH7/ref=sr_1_25?crid=XFW8ZXOZPV9J&dib=eyJ2IjoiMSJ9.BQ4Ax8MlqxR-PytMsB4nJCNjWGw9f1JDOZfhhKQSN46P5ikejPD8TuRQ7vgLowpkFrVKx_4H6KZucwunCrAGL5g8iZyzC-SpDnfK-i0JV_NPbvcZlF5G1NJ15WtYuskaHprzWmnfF5MECu_jQ9dYMtnh2DExWlUyMOExhxTdyQp5zI68uMmfAQIB11hxxoYxbG2dkkf83cBGvcplNtH_P3gYzcqtqVL6iMROXKREV-KFUmNbN4IWo1IlgDd71bXmpdD65LEM7o1vF5Y_QV9ppjTe3Sshs8Vkl1McWd2HIGo.FL5JO3D0AFgw-MuqSaV6Smjre_Ygrk4eIijKvK4g4_0&dib_tag=se&keywords=women%2Bkurtas&qid=1750670228&sprefix=women%2Bkurtas%2Caps%2C352&sr=8-25&th=1&psc=1")
        print("Please check the price on the website before continuing!")
        price = 1299
        qty = int(input("Enter quantity: "))
        add_to_cart("Kurtas", price, qty)
    elif ch==4:
        webbrowser.open_new("https://www.amazon.in/London-Hills-Cotton-Oversized-T-Shirts/dp/B0C8YKZ4W6/ref=sr_1_7?crid=HPVDO5RP70MS&dib=eyJ2IjoiMSJ9.VYKPGJa6y9-NDfzc93cVIqTzAYLluC_fPRd1ECOPd15826kYVUuAmafMoBVCdnUunvyQRNu4sdofcW9JrDVmVOG4KM_OgkRL1KNZhMdEkaUGELLNhdaXg28wtTjWghRqdMt5RrooZ7SIIGsUkiINpFzErX5A1psOnFXC-hToRoj6wGCsCeOYiZBMfQd5l-uPkRJKNIpTuO1fCF--YcJSttB7BELns5uOAH4N7QCocPpL5TrHvbRfA7eqZFCns3qITM3gvkJ5kTfWJPQVxNDgWUEGTugpbBSr5A5ttzQxwH0.b1NKUpbEHUk_Gu8F0f84vKdXzm6uKLd1AbomtplIE5U&dib_tag=se&keywords=women%2Btshirt%2Bcotton&qid=1750670306&sprefix=women%2Btshi%2Caps%2C393&sr=8-7&th=1&psc=1")
        print("Please check the price on the website before continuing!")
        price = 240
        qty = int(input("Enter quantity: "))
        add_to_cart("T-shirts", price, qty)
    else:
        print("Invalid choice")       
