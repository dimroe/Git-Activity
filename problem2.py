# Add comment to git Activity
# Fib suite to 1000000

a, b = 1, 2
resultat = 0
while b < 4000000:
    if b % 2 == 0:
        resultat += b
    a, b = b, a + b
print(resultat)
