'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.'''
import time
start_time = time.time()
sum = 0
for ii in range(0,1000):
    if ii%3==0 or ii%5==0:
        sum = sum + ii
print(sum)
print("--- %s seconds ---" % (time.time() - start_time))
