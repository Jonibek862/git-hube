hisoblash =lambda x,a,b,c: x-2*a+a**2*x*(b-c**2)

x=float(input("x ni kriting="))
a=float(input("a ni kriting="))
b=float(input("b ni kriting="))
c=float(input("c ni kriting="))

natija = hisoblash(x,a,b,c)
print(f"Natija:y={natija}")