#sort an array and return kth element
#take input file as command line argument and k value as command line argument

import sys

def main():

  # k = 5
  k = int(sys.argv[2])
  nums = []
  with open(sys.argv[1]) as f:
    for line in f:
      nums.append(int(line))

  nums.sort()
  # print 'array:', nums
  print 'element at index',k,':', nums[k]


if __name__ == "__main__":
    main()