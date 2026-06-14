import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase Letter Check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase Letter Check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number Check
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Password Strength Result
    if strength == 5:
        result = "Very Strong Password"
    elif strength >= 3:
        result = "Moderate Password"
    else:
        result = "Weak Password"

    return result, feedback


# Main Program
password = input("Enter your password: ")

result, suggestions = check_password_strength(password)

print("\nPassword Analysis Result:")
print(result)

if suggestions:
    print("\nSuggestions to Improve Password:")
    for item in suggestions:
        print("-", item)
