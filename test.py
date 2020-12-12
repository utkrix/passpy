def a():
    a = input("anyhting")
    b = input("koags")
    return a,b
    
def b(a,b):
    print(a,b)

def c():
    aa , bb = a()
    b(aa, bb)
c()