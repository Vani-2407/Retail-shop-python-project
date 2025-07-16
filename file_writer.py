from datetime import datetime

# Sample user/cart data
name = input("Enter your name: ")
phone = input("Enter your phone number: ")

# Sample cart
items = [
    {"name": "Casual Cotton Shirt", "qty": 2, "price": 799},
    {"name": "Formal White Shirt", "qty": 1, "price": 999}
]

# Total calculation
total = sum(item['qty'] * item['price'] for item in items)

# File creation
filename = f"bill_{name}.txt"
with open(filename, 'w') as f:
    f.write("🛍️ Retail Therapy Bill Receipt 🛍️\n")
    f.write("-----------------------------------\n")
    f.write(f"Customer Name : {name}\n")
    f.write(f"Phone Number  : {phone}\n")
    f.write(f"Date          : {datetime.now()}\n")
    f.write("-----------------------------------\n")
    f.write("Items Purchased:\n")
    for item in items:
        f.write(f"- {item['name']} x {item['qty']} = ₹{item['qty'] * item['price']}\n")
    f.write("-----------------------------------\n")
    f.write(f"Total Amount  : ₹{total}\n")
    f.write("Thank you for shopping with us!\n")

print(f"\n✅ Bill saved as '{filename}'!")
