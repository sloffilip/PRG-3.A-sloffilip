konec = int(input("Jaká bude konečná hodonta?"))

a = 0
b = 1
while b <= konec:
    print(a, " ", end="")
    print(b, " ", end="")
    a=a+b
    b=b+a
if a<=konec:
    print(a)
