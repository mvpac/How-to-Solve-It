# swapping two numbers using a temp variable 
a = 6
b = 5
temp = a
a = b
b = temp

print(a)
print(b)

##

# swapping without using temp variable
a = 3
b = 4
a = a+b #11
b = a-b #6
a = a-b

print(a)
print(b)


##
#swapping using python syntax

a = 8
b = 7

a,b = b,a
print(a)
print(b)

##
def swap(x,y):
    a = x
    b = y
    a = a+b
    b = a-b
    a = a-b
    print(a)
    print(b)
