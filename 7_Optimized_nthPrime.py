import time
def seive(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

start_time = time.time()
primes = list(seive(150000))
print(primes[10000])
print("--- %s seconds ---" % (time.time() - start_time))
