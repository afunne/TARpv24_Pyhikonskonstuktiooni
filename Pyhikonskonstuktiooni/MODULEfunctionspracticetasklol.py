import re

def registreerimine(username:str,paroolXD:str,tehe:int)->any:
    """
    See funktsion teeb või küsis kasutajanimist ja parolist
    """
    while True:
        if tehe in [1, 2]:
            pass
        else:
            print("*insert cat exploding gif*")
        if username is None:
            print("Nuh uh")
            continue
        else: pass

        if username.isalpha:
            pass
        else:
            print("Nuh uh")
            continue

        if username.isdigit:
            pass
        else:
            print("Nuh uh")
            continue
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
        if(regex.search(registreerimine) == None):
            print("Yuh uh")
        else:
            print("Nuh uh")
            continue

    return username, paroolXD, tehe