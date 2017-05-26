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
