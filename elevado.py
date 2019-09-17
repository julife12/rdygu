def hola1():
    for i in range(1,3 ):
        a=int(input("digite el numero: "))
        b=int(input("digite a que esta elevado"))
        cuadrado=1
        for j in range(1, b+1):
            cuadrado=cuadrado*a

        
        print(cuadrado)
        if i<2:
            x1=cuadrado
        else:
            x2=cuadrado

        
    if x1<= x2:
        print("el mayor fue: ", x2)
    else:
        print("el mayor fue: ", x1)



hola1()