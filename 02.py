n = 12
a, b, c = 0, 1, 1

while a < n:
    if a == n or b == n or c == n:
        print(f"O número {n} pertence à sequência de Fibonacci.")
        break
    a = b + c
    b = c + a
    c = a + b
else:
    print(f"O número {n} não pertence à sequência de Fibonacci.")
