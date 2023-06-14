import re



def password_strength(password):
    
    rating = 0
    
    if len(password) < 8:
        return "Weak Password Change it !"
    elif len(password) >= 12:
        rating += 2
    else:
        rating +=1
        
        
    # to check upprercase case in Password
    if re.search(r'[A-Z]', password):
        rating += 1
        
    # to check lowercase cas in password
    if re.search(r'[a-z]', password):
        rating += 1

 # Check for dig 
    if re.search(r'\d', password):
        rating += 1

    # Check for symb
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        rating += 1

    # Return the password ratings
    if rating < 3:
        return "weak"
    elif rating < 5:
        return "medium"
    else:
        return "strong"







# here where all thr magic happens
password = input("Enter a password: ")
strength = password_strength(password)
print("Password strength: " + strength)