import time
import sys
import winsound
from otp_generate import otp_verification_flow

def animation():
    print("\nRedirecting to payment gateway", end="")
    for _ in range(5):
        time.sleep(0.4)
        print(" 💖", end="")
        sys.stdout.flush()
    print("\n")

def sound():
    frequency = 800
    duration = 500
    winsound.Beep(frequency, duration)

def payment_gateway():
    # Step: OTP verification before payment
    if not otp_verification_flow():
        print("⛔ OTP verification failed. Payment cancelled.")
        return False
    else:
        print("✅ OTP Verified! Proceeding to payment...")

    animation()
    print("💳 Welcome to the Payment Gateway")
    print("---------------------------------")
    print("1. UPI")
    print("2. Debit/Credit Card")
    print("3. Net Banking")
    print("4. Cash on Delivery (COD)")
    print("5. Cancel Payment")

    choice = input("Choose a payment option (1-5): ").strip()

    if choice == "5":
        print("\n❌ Payment cancelled.")
        return False

    elif choice == "4":
        print("\n📦 Order placed with Cash on Delivery option.")
        sound()
        print("🛍️ Thank you for shopping with Retail Therapy! 💕")
        return True

    # For UPI, Card, Net Banking
    print("\nProcessing your payment", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    time.sleep(1)

    sound()
    print("\n✅ Payment successful!")
    print("🛍️ Thank you for shopping with Retail Therapy! 💕")
    return True
