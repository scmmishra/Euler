'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Notes:
Brute approach: Test all integers less than n until a divisor is found.
Improvisation: Test all integers less than root of n
A faster approach will be using Pollard's Rho Algorithm
'''

import time
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
    number = 600851475143
    for ii in reversed(range(1, int(number**0.5)+1)):
        if number%ii==0 and is_prime(ii):
            print(ii)
            break
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
