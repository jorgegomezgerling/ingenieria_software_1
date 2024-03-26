import matplotlib.pyplot as plt

def collatz_count(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

results = []
for num in range(1, 10001):
    count = collatz_count(num)
    results.append((num, count))

# Mostrar el resultado en la consola
for num, count in results:
    print(f"Número: {num}, Iteraciones: {count}")

# Crear el gráfico
x_values = [count for num, count in results]
y_values = [num for num, count in results]
plt.scatter(x_values, y_values)
plt.xlabel('Iteraciones')
plt.ylabel('Número Inicial')
plt.title('Número de Collatz para Números entre 1 y 10000')
plt.grid(True)
plt.show()
