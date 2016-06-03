#quickselect

import sys
import rand

def quickselect(A, k):
		r = rand.range(1,len(A)) #   let r be chosen uniformly at random in the range 1 to length(A)
		pivot = A[r]  #   let pivot = A[r]
		left = [for x in A if x < A[r]] #array of smallest elements
		right = [for x in A if x > A[r]] #array of largest elements
		if(k <= len(left)):
				return quickselect(left, k)
		if(k > (len(A) - len(right))):
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
  quickselect(nums, k)




if __name__ == "__main__":
    main()
