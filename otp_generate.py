# otp_generate.py
from twilio.rest import Client

# 🪪 Twilio credentials (get these from https://www.twilio.com/console)
account_sid = "AC7278e4a5d2e5f7c5097089f45a0fb319"
auth_token = "84b21b34210f937c68e4ef8a695a45df"

# Create Twilio client
client = Client(account_sid, auth_token)


def otp_verification_flow(to_number):
    """
    Sends an OTP using Twilio Verify service and verifies user input.
    Returns True if OTP verified successfully, else False.
    """

    try:
        # Step 1: Create a Verify Service (Twilio handles OTP automatically)
        service = client.verify.v2.services.create(friendly_name="Retail Therapy OTP")
        verify_sid = service.sid

        # Step 2: Send OTP
        client.verify.v2.services(verify_sid).verifications.create(to=to_number, channel="sms")
        print("✅ OTP sent successfully!")

        # Step 3: Ask for OTP input
        otp_input = input("🔐 Enter the OTP you received: ").strip()

        # Step 4: Verify OTP
        check = client.verify.v2.services(verify_sid).verification_checks.create(to=to_number, code=otp_input)

        if check.status == "approved":
            print("🎉 OTP Verified Successfully!")
            return True
        else:
            print("❌ Incorrect OTP. Try again.")
            return False

    except Exception as e:
        print("❌ Error during OTP process:", e)
        return False


# Optional: test OTP flow directly if you run this file alone
if __name__ == "__main__":
    to_number = input("📲 Enter your verified number (like +916369733236): ").strip()
    otp_verification_flow(to_number)
