def register_user(user):
    return {
        "message": "User Registered",
        "user": user
    }

def login_user(user):
    return {
        "message": "Login Successful",
        "email": user.email
    }