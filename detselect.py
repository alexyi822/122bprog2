#deterministic select


#https://www.ics.uci.edu/~eppstein/161/960130.html



import sys


def deterministic_select(L, k):
    if(L < 10):
        L.sort() #uses quicksort or bubblesort iirc
        return L[k]
    x = []
    for( i in (len(L)/5)):
        x[i] = select(L[i], 3)

    M = select(L[i], (len(n)/10))

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




if __name__ == "__main__":
    main()
