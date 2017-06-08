"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


Solution
There are two ways to do it, both involve some looping and s0me summation and series formulas
Method Number one
Use summation formula

(Summation of An)   =   Summation of An^2 + Summation(Summation of Ai*Aj)
    n=1 to N                n=1 to N        j=1 to N  i=1 to j-1

So solving the second term gives us the difference and hence our answer
This can work for any numbers in a list however since we need to work for first n natural numbers, these many loops are unnecessary.
The other way around this is using series formulas which brings us to Method Number 2

Method Number two

Summation of first n numbers = ((n^2) + n) / 2  .........................(1)
Summation of squares of first n numbers = (2*(n^3) + 3*(n^2) + n)/6 .....(2)

So the answer is equation (2) subtracted by square of equation (1)
We use method two here

"""
import time
import math
start_time = time.time()
n=100
n2=10000
value = (n*(n2 - 1)*(3*n + 2))/12
print(value)
print("--- %s seconds ---" % (time.time() - start_time))
