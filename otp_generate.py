from twilio.rest import Client
import random

# Twilio credentials (replace with your actual details)
account_sid = 'AC7278e4a5d2e5f7c5097089f45a0fb319'
auth_token = 'efbd6dd3fbc3c2678b19fe95e87b89cc'
twilio_number = '+18563867305'

# Generate a 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Send OTP to the given number
def send_otp(to_number):
    client = Client(account_sid, auth_token)
    otp = generate_otp()

    try:
        message = client.messages.create(
            body=f"🛍️ Retail Therapy OTP: {otp}",
            from_=twilio_number,
            to=to_number
        )
        print(f"✅ OTP sent successfully! SID: {message.sid}")
        return otp
    except Exception as e:
        print("❌ Error sending OTP:", e)
        return None

# Complete OTP verification process
def otp_verification_flow():
    print("📲 Please enter your verified mobile number in format +91XXXXXXXXXX")
    to_number = input("Enter your mobile number: ").strip()

    # Validate format
    if not (to_number.startswith("+91") and len(to_number) == 13 and to_number[1:].isdigit()):
        print("❌ Invalid number format! Must be +91 followed by 10 digits.")
        return False

    otp = send_otp(to_number)

    if otp is None:
        print("❌ Failed to send OTP. Please check your number or try again later.")
        return False

    entered_otp = input("🔐 Enter the OTP you received: ").strip()

    if entered_otp == otp:
        print("✅ OTP Verified Successfully!")
        return True
    else:
        print("❌ Incorrect OTP. Payment cannot proceed.")
        return False
