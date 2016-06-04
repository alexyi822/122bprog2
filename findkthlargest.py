#sort an array and return kth element
#take input file as command line argument and k value as command line argument
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html

import time
import sys
comp = 0 # number of comparisons


def insertion_sort(arr):
  global comp
  for index in range(1, len(arr)):
    currentValue = arr[index]
    pos = index

    while pos > 0 and arr[pos-1] > currentValue:
      comp = comp+1
      arr[pos]=arr[pos-1]
      pos=pos-1

    arr[pos] = currentValue

def main():
  start = time.clock()
  

  # k = 5
  k = int(sys.argv[2])
  nums = []
  with open(sys.argv[1]) as f:
    for line in f:
      nums.append(int(line))

  # nums.sort()
  insertion_sort(nums)
  end = time.clock()
  print("kth element:\t %d" % (nums[k-1]))
  print("Comparisons:\t %d" % (comp))
  print("Time:\t %f" % (end-start))


if __name__ == "__main__":
    main()