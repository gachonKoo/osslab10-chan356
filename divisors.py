def divisors(n: int):
    return [i for i in range(1, n + 1) if n % i == 0]


def get_divisors(n: int):
    return divisors(n)

if __name__ == "__main__":
    n = int(input())
    print(" ".join(str(x) for x in divisors(n)))
