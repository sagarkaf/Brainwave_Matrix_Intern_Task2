import re
import string

def check_password_strength(password):
    feedback = []

    # 1. Length Check
    if len(password) < 8:
        feedback.append("Password is too short.")
    elif len(password) > 20:
        feedback.append("Password is too long.")

    # 2. Complexity Check
    # Check for uppercase letter
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letter
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    special_characters = string.punctuation
    if not any(char in special_characters for char in password):
        feedback.append(f"Password should contain at least one special character.")

    # 3. Uniqueness Check
    # Common password patterns to check, including the new ones
    common_patterns = [
        "1234", "password", "qwerty", "letmein", "abc123", 
        "welcome", "admin", "12345", "sagar123", "kafle123", "123456"
    ]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Password contains common or easily guessable patterns.")
    
    # Check for simple sequential characters like "123", "abc"
    if re.search(r'(123|abc|qwerty|password|letmein)', password.lower()):
        feedback.append("Password contains simple sequential characters or common words.")
    
    # Check for repeated characters (e.g., "aaaa", "1111")
    if len(set(password)) < len(password) / 2:
        feedback.append("Password contains repeated characters.")

    # 4. Final Feedback
    if not feedback:
        feedback.append("Password is strong.")
    else:
        feedback.append("Your password is weak. Consider improving it by following the recommendations above.")

    return feedback

# Example usage:
password = input("Enter your password: ")
strength_feedback = check_password_strength(password)

for feedback in strength_feedback:
    print(feedback)
