#quickselect

import sys

def main():
  k = int(sys.argv[2])
  nums = []
  with open(sys.argv[1]) as f:
    for line in f:
      nums.append(int(line))

  


if __name__ == "__main__":
    main()