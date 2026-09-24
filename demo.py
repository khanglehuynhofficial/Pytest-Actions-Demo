import re

def validate_secure_password(password: str) -> bool:
    if len(password) < 8 or len(password) > 20:
        return False
    if " " in password:
        return False
    if not re.search(r"[A-Z]", password): 
        return False
    if not re.search(r"[a-z]", password): 
        return False
    if not re.search(r"[0-9]", password): 
        return False
    if not re.search(r"[@#$%^&+=!_?*()\-+~.`,;:\[\]{}<>\\/|]", password): 
        return False
    return True

