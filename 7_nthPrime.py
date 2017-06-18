import time
import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


def main():
    start_time = time.time()
    primes=[2]
    isPrime = True
    n = 1
    for ii in range (3, 1000000, 2):
        if is_prime(ii):
            primes.append(ii)
            n = n + 1
        if n == 10001:
            break
    print(primes[10000])          
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
