import time
def seive(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
start_time = time.time()
print(sum(list(seive(2000000))))
print("--- %s seconds ---" % (time.time() - start_time))
