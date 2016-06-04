#deterministic select


#https://www.ics.uci.edu/~eppstein/161/960130.html



import sys


def deterministic_select(L, k):
    if(L < 10):
        L.sort() #uses quicksort or bubblesort iirc
        return L[k]




    subs = [L[i:i+5] for i in xrange(0, len(L), 5)] # partitions in n/5 groups of length at most 5
    x = []
    for y in range(0,(len(L)/5)):
        x[y] = deterministic_select(subs[y], 3)

    M = deterministic_select(x, (len(L)/10))

    left = [x for x in L[i] if L[i] < M]
    right = [x for x in L[i] if L[i] > M]
    center = [x for x in L[i] if L[i] == M]

    if(k <= len(left)):
            return select(left,k)
    if(k > len(left)+len(center)):
            return(right, k-len(left)-len(center))
    else:
            return M

def main():
  k = int(sys.argv[2])
  nums = []
  with open(sys.argv[1]) as f:
    for line in f:
      nums.append(int(line))
  x = deterministic_select(nums, k)
  print(x)



if __name__ == "__main__":
    main()
