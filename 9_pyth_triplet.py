import time
def solve():
    for aa in range (1,1000):
        for bb in range (aa,1000-aa):
            cc = 1000 - aa - bb
            if (aa*bb) + (1000*cc) == 500000:
                return(aa*bb*cc)
start_time=time.time()
print(solve())
print("--- %s seconds ---" % (time.time() - start_time))
