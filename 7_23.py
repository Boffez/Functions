###
# A function that returns True if the password is correct
# nce
#

def f(password):
    sign = []
    if len(password) >= 6:
        for i in password:
            if i not in sign:
                sign.append(i)
            else:
                return False
    else:
        return False
    return True


print(f('ax15'))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(''))