#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass 

    def run(self, min_num, max_num):
        results = []
        for num in range(min_num, max_num + 1):
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            results.append(fact)
        return results
    
if __name__ == "__main__":
    factorial_calculator = Factorial()
    min_num = int(input("Ingrese el número mínimo: "))
    max_num = int(input("Ingrese el número máximo: "))
    results = factorial_calculator.run(min_num, max_num)
    print("Factoriales calculados:", results)
