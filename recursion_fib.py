def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


n = int(input("ededi daxil edin :"))
print(f"{n}ci fibonacci ededi = {fibonacci(n)}")
