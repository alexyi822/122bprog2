#quickselect

import sys
import random
comp = 0 # number of comparisons

def quickselect(A, k):
		if len(A) < 2:
				return A[0]
		r = random.randint(1,len(A)-1) #   let r be chosen uniformly at random in the range 1 to length(A)
		pivot = A[r]  #   let pivot = A[r]
		left = [x for x in A if x < A[r]] #array of smallest elements
		right = [x for x in A if x > A[r]] #array of largest elements
		comp += len(A)
		comp += 3 # for the if statments
		if(k <= len(left)):
				comp -= 2 # didnt compare the other if and else
				return quickselect(left, k)
		if(k > (len(A) - len(right))):
				comp -= 1 # didnt compare the last else
				return quickselect(right, k - (len(A) - len(right)))
		else:
			#it's equal to the pivot
			return pivot


def main():
  k = int(sys.argv[2])
  nums = []
  with open(sys.argv[1]) as f:
    for line in f:
      nums.append(int(line))
  kth = quickselect(nums, k)
  print("kth element is %d" % (kth))
  print("Comparisons:\t %d" % (comp))



if __name__ == "__main__":
    main()
