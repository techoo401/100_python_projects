SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.<>?/"


def check_password(password):

    score = 0
    suggestions = []

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters")

    # Check each character
    for char in password:

        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in SPECIAL_CHARACTERS:
            has_special = True

    # Score based on character types
    if has_upper:
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    if has_lower:
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one number")

    if has_special:
        score += 1
    else:
        suggestions.append("Add at least one special character")

    # Determine strength
    if score <= 2:
        strength = "VERY WEAK"

    elif score <= 4:
        strength = "WEAK"

    elif score == 5:
        strength = "MEDIUM"

    else:
        strength = "STRONG"

    return score, strength, suggestions


def main():

    print("=" * 50)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("Enter password: ")

    score, strength, suggestions = check_password(password)

    print("\n" + "-" * 50)
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/6")
    print("-" * 50)

    if suggestions:

        print("\nSuggestions:")

        for suggestion in suggestions:
            print(f"- {suggestion}")

    else:
        print("\nYour password satisfies all basic requirements!")


if __name__ == "__main__":
    main()