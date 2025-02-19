def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
n = 2
while len(primos) < 15:
    if es_primo(n):
        primos.append(n)
    n += 1

print(primos)