#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verificar si se proporcionó el rango como argumento en la línea de comandos
if len(sys.argv) < 2:  
    range_str = input("Ingrese un rango de números (desde-hasta) para calcular los factoriales: ")
else:
    range_str = sys.argv[1]

# Separar el rango en los números desde y hasta
range_parts = range_str.split("-")
if len(range_parts) != 2:
    print("Formato de rango incorrecto. Debe darse un rango")
    sys.exit(1)

from_num = int(range_parts[0])
to_num = int(range_parts[1])

# Calcular los factoriales dentro del rango
for num in range(from_num, to_num + 1):
    print("Factorial de", num, "! es", factorial(num))



