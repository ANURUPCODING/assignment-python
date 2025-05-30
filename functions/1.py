def is_prime(num):
    if num < 2:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True

def primes_between(start, end):
    primes = []
    num = start
    while num <= end:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

start = int(input("Start: "))
end = int(input("End: "))

print("Prime numbers:")
print(primes_between(start, end))
