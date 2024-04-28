def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
    
owner = "Miguel"
name = "Miguel"
print(greet(name, owner))
