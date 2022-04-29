# 3rd part of loop
# in we take value for user for loop

'''while True:
    n = int(input("what's n?"))
    if n > 0:
        break #it break the code
    
for _ in range(n):
    print("hello")
#Now the user add any number like 10 then the hello will print 10 time and it sam on other value also 
'''
'''
def main():
    hello(4)#in brakect we add number it print that much time onlys

def hello(n):
    for _ in range(n):
        print("HELLO")
main() # we call main that we set on def
'''
#it same code and it work same
def main():
    number = get_number()
    hello(number)

def get_number():
    while True:
        n = int(input("what's x?"))
        if n > 0:
            break
    return n 

def hello(n):
    for _ in range(n):
        print("HELLO")
    
main()