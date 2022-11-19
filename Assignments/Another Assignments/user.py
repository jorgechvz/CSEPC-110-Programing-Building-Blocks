#create the funtion for user

def user(nickname):
    long = len(nickname)
    x = nickname.isalnum()
    if x ==False:
        print("the nickname only have a alpha and numeric caracteres")
    elif long 