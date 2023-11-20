def areaOfSquare(l):
    return l**2
def volumeOfSphere(r):
    return float((4/3)(3.1415)(r**3))
def areaOfSphere(r):
    return float((4/3)(3.1415)(r**2))
def areaOfTriangle(w,h):
    return float(1/2(w*h))
def areaOfEquilateral(a):
    return float(((3**1/2)/4)*a**2)
def fibbo(n):
    num1 = 0
    num2 = 1
    next_number = num2 
    count = 1
    print("0",end="")
    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()

def tuppleTOList(tpl):
    tlist = []
    for i in tpl:
        tlist.append(i)
    return tlist
def evenInTupple(tpl):
    count = 0
    for i in tpl:
        if i % 2 == 0:
            count+=1
    return count
def greaterThan20(tpl):
    tlist = []
    for i in tpl:
        if i > 20 : 
            tlist.append(i)
    return tlist
        
