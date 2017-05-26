'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Algorithm (-_-)

n is a palindorme
(1000-a)(1000-b) = n
1000000 - 1000(a+b) + ab = n
1000(1000 - (a+b)) + ab = n

Now if we assume ab < 1000 i.e. ab is 3 digit
So first three digits on n are 1000 - (a+b)
Next three digits are ab

Let the palindrome be of the form xyzzyx
Therefore   100x + 10y + z = 1000 - (a+b) ................(1)
            100z + 10y + x = ab ..........................(2)

Solving eq 1 and 2
    100x + 10y +    z =   1000 - a - b
     - x - 10y - 100y = - ab
----------------------------------------
99x - 99z = 1000 - a - b - ab
            OR
99z - 99x = a + b + ab - 1000

Solving further
(z-x) = (1/99)(a+b+ab-1000)
(z-x) = (1/99)(a+b+ab-10) - (990/99)
(z-x) = (1/99)(a+b+ab-10) - 10
(z-x) = (1/99)(a+b+ab+1-11) - 10
now x can be any number from -9 to 0 since z-x shouldnt be negative

Now a+b+ab+1-11 has to be divisible by 99
Therefore a+b+ab+1-11=99p
a+b+ab+1=99p-11
(a+1)(b+1)= 11(9p-1)

lets call 9p-1 the magic_factor
'''
import time
def palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    start_time = time.time()
    for p in range(0,9):
        magic_factor = 9*p - 1
        for jj in range(1,magic_factor):
            a = 1001 - magic_factor/jj
            b = 1001 - 11*jj
            if palindrome(a*b):
                print(a*b, a, b)
                break

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
