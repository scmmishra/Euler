"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Solution:
This experiment will help you understand the Algorithm
Lets look at all prime factor from 1 to 10
1   []
2   [2]
3   [3]
4   [2, 2]
5   [5]
6   [2, 3]
7   [7]
8   [2, 2, 2]
9   [3, 3]
10  [2, 5]

So if we multiple all these numbers but condering the occurance of the numbers, ie their multiplicity in a list.....
So we can merge the list...
Supposing when we merge factors of 2 and 4, we include '2' from 2nd and from 4th we take only one '2' since there already exist another '2'
so the merged list becomes
[2,3,2,5,7,2,3] the product is 2520

So when merging we look for an number, subtract their occurances in the both the lists, and add that many numbers of that element in the list
"""

import time
def factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n/2
    p = 3
    while n != 1:
        while n % p == 0:
            factors.append(p)
            n = n/p
        p += 2
    return factors

def factor_append(factors,new):
    if len(factors) == 0: return new
    for i in range(len(new)):
        if i > 0 and new[i] == new[i-1]: continue
        new_count = new.count(new[i])
        old_count = factors.count(new[i])
        if new_count > old_count:
            for j in range(new_count - old_count): factors.append(new[i])
    factors.sort()
    return factors

def main():
    start_time = time.time()
    num = 20
    F = []
    for i in range(1,num + 1):
        F = factor_append(F,factors(i))
    product = 1
    for i in F: product *= i
    print(product)
    print("--- %s seconds ---" % (time.time() - start_time))
