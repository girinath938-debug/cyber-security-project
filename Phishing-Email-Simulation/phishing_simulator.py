# Phishing Email Simulation
# Educational Purpose Only

phishing_keywords = [
    "urgent",
    "verify your account",
    "click here",
    "bank account",
    "password",
    "win prize",
    "free money",
    "login immediately"
]

def check_email(email):
    email = email.lower()
    found = []

    for keyword in phishing_keywords:
        if keyword in email:
            found.append(keyword)

    if found:
        print("\n⚠ Warning: Suspicious Email Detected!")
        print("Possible phishing keywords found:")
        for item in found:
            print("-", item)
    else:
        print("\n✅ Email appears safe.")


# Main Program
print("=== Phishing Email Awareness Simulator ===")

email_text = input("\nEnter email content:\n")

check_email(email_text)
