def suma(num1,num2):
    a = isinstance(num1, int)
    b = isinstance(num2, int)
    
    if not a or not b :
        raise TypeError("Variable no es un número")

    x = num1+num2
    
    return x

def resta(num1,num2):
    a = isinstance(num1, int)
    b = isinstance(num2, int)
    
    print(a,b)
    
    if not a or not b:
        raise TypeError("Variable no es un número")

    x = num1-num2
    return x

def producto(num1,num2):
    a = isinstance(num1, int)
    b = isinstance(num2, int)
    print(a,b)
    if not a or not b:
        raise TypeError("Variable no es un número")

    x = num1*num2
    return x

    

def division(num1,num2):
    a = isinstance(num1, int)
    b = isinstance(num2, int)
    if not a or not b:
        raise TypeError("Variable no es un número")

    if num2==0:
        raise ZeroDivisionError("Error al intentar dividir por 0")
    
    else:
        x=num1/num2
        return x


