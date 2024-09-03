# Names: Bernardo Haba, Érico Panazzolo, Henrique Brauveres e Luana Thomas.

import matplotlib.pyplot as plt

def linear_congruential_generator(seed, a, c, m, n):
    numbers = []
    x = seed
    for _ in range(n):
        x = (a * x + c) % m
        # numbers.append(x)
        numbers.append(x / m) 
    return numbers

seed = 379 # seed
a = 1238123 # mult
c = 1293921 # incr
m = 1340459862 # mod
n = 1000     

ps_random_numbers = linear_congruential_generator(seed, a, c, m, n)

for num in ps_random_numbers:
    print(num)

plt.scatter(range(n), ps_random_numbers, s=1)
plt.title('Gráfico de Dispersão de Números Pseudoaleatórios')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.show()
