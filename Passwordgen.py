
import random  #imports a random number.
import string  #imports a string of characters.

def generate_password(length: int = 10):  #a function called generate passsword and sets the lenght to 10
    alaphabets = string.ascii_letters + string.digits + string.punctuation # created a variable called alaphabets that contains letters, digits and punctuation.
    password  = ''.join(random.choice(alaphabets) for _ in range(length)) # creates a variable called password that joins the random letters and digits together.
    return generate_password  #returns the function

password = generate_password() #calls the function and set it to a variable called password
print(f"Generated Password: {password}") # prints the generated password