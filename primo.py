def hola2(a):
    divisores=0
    mitadE=a//2
    for i in range(1, mitadE+1):
        if a%i==0:
            divisores=divisores+1


    if divisores<2:
        print("el numero es primo")
    else:
        print("el numero no es primo") 

x=int(input("El numero a probar es: "))
hola2(x)