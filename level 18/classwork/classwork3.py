name = "admin"
password = "adminpassword123"

user = input("please enter your name: ")

if user == name:
    pass_ = input("please enter your password: ")
    if pass_ == password:
        print("სალამი ადმინ!")
    else:
        print("წვდომა არ გაქვს")
else:
    print("სალამი მომხმარებელო")
