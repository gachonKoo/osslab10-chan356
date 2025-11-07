n = int(input())
divs = []

for i in range(1, n + 1):
    if n % i == 0:
        divs.append(str(i))

print(" ".join(divs))
