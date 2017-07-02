import time
with open('Output.txt') as f:
    primes = text_file.read().split(',')
def triangular(n):
    return sum(range(n+1))

def prime_before(number):
    if number == 1:
        return 1
    elif number in primes:
        return number
    else:
        return prime_before(number - 1)

def calculate(rawlist):
    yo = 1
    for jj in rawlist:
        yo = yo * (jj+1)
    return yo

def main():
    num = 0
    count = 0
    count_list = []
    for ii in range (5,100):
        num = triangular(ii)
        num2 = num
        print(num, end=" ")
        largest_prime = prime_before(num)
        for ii in reversed(primes[:primes.index(largest_prime)+1]):
            while num % ii == 0:
                count = count + 1
                num = num / ii
            if count != 0: count_list.append(count)
            count = 0
        print(calculate(count_list))
        if calculate(count_list) == 500:
            return num2
        del count_list[:]

if __name__ == "__main__":
    main()
