# Q1
print("*********Q1*********")
def q1(s1):
    s1 = "tom " + s1
    return s1

a = q1("brady")
print(a)
print("********************")
print(" ")


# Q2
print("*********Q2*********")
def q2(s2):
    length = len(s2)
    return length

b = q2("a string")
print("the length of the string is: ", b)
print("********************")
print(" ")


# Q3
print("*********Q3*********")
def q3(n1):
    if (n1 % 2 == 0):
        return "even"
    else:
        return "odd"

c = q3(9)
print("the number entered is ", c)
print("********************")
print(" ")


# Q4
print("*********Q4*********")
def q4(s3):
    reversed = s3[::-1]
    return reversed 

d = q4("reverse this string")
print("reversed string: ", d)
print("********************")
print(" ")


# Q5
print("*********Q5*********")
def primary(s4):
    f = secondary(s4)
    f += "see, ya"
    return f

def secondary(s5):
    newString = s5 + "gday, mate "
    return newString

e = primary("hello ")
print(e)
print("********************")
print(" ")