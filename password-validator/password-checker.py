def basic_password_check(password):
    min_length = 15  # NIST 800-63B single factor password guidance
    # Check length
    if len(password) < min_length:
        return f"Password needs to have a minimum length of {min_length} characters. Password only has {len(password)}."

    # 2. Check for at least one digit (basic complexity)
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number (0-9)."

    return "Password passes basic checks: sufficient length and contains at least one number."

if __name__ == "__main__":
    password = input("Enter a password to test: ")
    result = basic_password_check(password)
    print(result)
