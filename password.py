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
    
    