def root_ex(a,b,c):
    r1= (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2= (-b-(b**2-4*a*c)**0.5)/(2*a)
    return r1, r2

a = 2
b = -1
c = -6

x_1 , x_2 = root_ex(a, b, c)
print(x_1 ,x_2)

'''
a=int(input("A입력: "))
b=int(input("B입력: "))
c=int(input("C입력: "))
# (a*x^2)+(b*x)+c
r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print(r1, r2)
def print_root_ex(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print(r1, r2)
print_root_ex(1,2,-8)
'''
