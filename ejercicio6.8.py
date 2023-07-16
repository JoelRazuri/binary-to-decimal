"""
    Escribir una función que reciba una cadena de unos y ceros (es decir, un número en representación binaria) y devuelva el valor decimal correspondiente.
"""

def binario_a_decimal(num_binario):
    # Recibe una cadena de unos y ceros (numero binario) y devuelve el valor decimal correspondiente.

    num_decimal = 0
    longitud = len(num_binario)

    for i in range(0,longitud):
        num_decimal = num_decimal + (int(num_binario[longitud-1]) * 2**i) # "longitud-1" recorre la cadena desde el final al comienzo para ir multiplicando por cada potencia de 2 que le corresponde
        longitud-=1
    
    return num_decimal


print(binario_a_decimal("11010"))
print(binario_a_decimal("11001100"))