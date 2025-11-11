import time
import sys
import winsound
from otp_generate import otp_verification_flow  # Import the OTP function

def animation():
    print("💳 Processing payment", end="")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\n")

def sound():
    # Beep sound to simulate payment confirmation
    try:
        winsound.Beep(1000, 200)
        winsound.Beep(1200, 200)
    except:
        pass

def payment_gateway():
    print("\n🧾 Payment Gateway Initiated...")
    print("📲 Please enter your verified mobile number in format +91XXXXXXXXXX")
    to_number = input("Enter your mobile number: ").strip()

    if not (to_number.startswith("+91") and len(to_number) == 13 and to_number[1:].isdigit()):
        print("❌ Invalid number format! Must be +91 followed by 10 digits.")
        return False

    # ✅ Corrected logic here
    verified = otp_verification_flow(to_number)
    if not verified:
        print("⛔ OTP verification failed. Payment cancelled.")
        return False

    print("✅ OTP verified successfully! Proceeding with payment...")
    animation()
    sound()
    print("🎉 Payment Successful! Thank you for shopping with us 🛍️")
    return True


# Optional: run only if this file is executed directly (not imported)
if __name__ == "__main__":
    payment_gateway()
