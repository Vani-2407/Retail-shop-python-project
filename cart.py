import os

cart = []

def add_to_cart(product_name, price, quantity):
    total = price * quantity
    cart.append({
        'product': product_name,
        'price': price,
        'qty': quantity,
        'total': total
    })

def show_cart(user_name, phone_number):
    print("\n🧾 Receipt -Your bill amount:")
    print(f"Customer: {user_name}")
    print(f"Phone: {phone_number}\n")

    grand_total = 0
    filename = f"bill_{user_name}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("🛍️ Retail Therapy Bill Receipt 🛍️\n")
        f.write("---------------------------\n")
        f.write(f"Customer: {user_name}\n")
        f.write(f"Phone: {phone_number}\n\n")
        f.write("Items:\n")

        for item in cart:
            line = f"{item['qty']} x {item['product']} @ ₹{item['price']} = ₹{item['total']}\n"
            print(line.strip())
            f.write(line)
            grand_total += item['total']

        f.write("\n---------------------------\n")
        f.write(f"Total Amount: ₹{grand_total}\n")
        f.write("---------------------------\n")
        f.write("Thank you for shopping with us! 🛍️\n")

    print("\n---------------------------")
    print(f"Total Amount: ₹{grand_total}")
    print("---------------------------")
    print("Thank you for shopping with us! 🛍️")
    print(f"\n✅ Bill saved to file: {filename}")

    # Optional: auto-open the bill file in Notepad (Windows only)
    try:
        os.system(f"notepad {filename}")
    except:
        pass
