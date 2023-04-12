lado1=int(input("ingrese perimer lado" " " ))
lado2=int(input("ingrese segundo  lado"  " "))
lado3=int(input("ingrese tecer lado" " "))

if lado1+lado2>lado3 and lado3+lado2>lado1 and lado1+lado3>lado2:
    print("es un triangulo") 

    if lado3==lado2==lado1:
    
        print("es equilatero")
    elif lado1==lado3 or lado2==lado1 or lado3==lado2:
        print("es isoseles") 
    else:
        print("es escaleno")    

else:print ("no es un triangulo valido")        