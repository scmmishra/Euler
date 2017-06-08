'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Brute force approach
'''
import time
def palindrome(num):
    return str(num) == str(num)[::-1]

def main():
    start_time = time.time()
    max_palin = 0
    for ii in reversed(range(100,999)):
        for jj in reversed(range(100,999)):
            if palindrome(ii*jj):
                if ii*jj > max_palin:
                    max_palin = ii*jj
    print(max_palin)
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
