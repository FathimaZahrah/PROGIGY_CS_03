import re

def assess_password_strength(password):
   
    length_ok = len(password) >= 8
    upper_ok = re.search(r'[A-Z]', password) is not None
    lower_ok = re.search(r'[a-z]', password) is not None
    number_ok = re.search(r'[0-9]', password) is not None
    special_ok = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    
    criteria_met = sum([length_ok, upper_ok, lower_ok, number_ok, special_ok])

    # Assess the strength of the password
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    feedback = []
    if not length_ok:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_ok:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_ok:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_ok:
        feedback.append("Password should contain at least one number.")
    if not special_ok:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

def main():

    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")
    else:
        print("Your password meets all criteria!")

if __name__ == "__main__":
    main()
