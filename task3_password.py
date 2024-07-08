import random
import string

def generate_password(length):
    # Define the character sets to use in generating the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password randomly
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage:
password_length = 12  # You can adjust the length as needed
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
