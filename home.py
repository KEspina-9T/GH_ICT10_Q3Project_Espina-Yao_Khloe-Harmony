from pyscript import display, document

def account_creation(e):
    document.getElementById('output').innerHTML = " "

    username = document.getElementById('username').value
    password = document.getElementById('pass').value

    if len(username) > 7: 
        if password.isdigit() and password.isalpha():
            display(f"your account has been created", target="output")

        elif len(password) >= 10 and password.isdigit() or password.isalpha():
            display(f"your password is too weak. please include both numbers and letters", target="output")
        else:
            display(f"your account has been created successfully!", target="output")

    elif len(username) < 7:
        display(f"your username is too short. please make it at least 7 characters long", target="output")

    else: 
        display(f"your account has been created successfully!", target="output")
