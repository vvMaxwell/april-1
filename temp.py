'''    Program to convert C to F '''
def celcius_to_fahrenheit(c):
    '''convers celcius to fahrenheit'''
    f = c * 9/5 + 32
    return f

def fahrenheit_to_celcius(f):
    '''convers celcius to fahrenheit'''
    c = f -32 *5/9
    return c

c = 25
f = 82
f = celcius_to_fahrenheit(c)
print(f"{c} degrees is {f} fahrenheit")

c = fahrenheit_to_celcius(f)
print(f"{f}degrees fahrenheit is {c} celcius")