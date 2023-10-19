'''
    Program to convert C to F
'''
def celcius_to_fahrenheit(c):
    '''convers celcius to fahrenheit'''
    f = c * 9/5 + 32
    return f
c = 25
f = celcius_to_fahrenheit(c)
print(f"{c} degrees is {f} fahrenheit")