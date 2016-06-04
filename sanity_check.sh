#!/bin/bash

#should generate a random k value
#findkthlargest.py: findkthlargest.py input-file k-value

RANGE=1000000
numInts=1000


#generate test files
mkdir sanity_check_test_cases

#generate 100 test files with 1000 integers in range [1, 10^6]
for i in {1..100}
do
  touch sanity_check_test_cases/test-${i}
  for j in {1..1000}
  do
    number=$(($RANDOM % $RANGE + 1))
    echo $number >> sanity_check_test_cases/test-${i}
  done
  #generate random k and run all 3 algorithms
  k=$(($RANDOM % $numInts))
  python findkthlargest.py sanity_check_test_cases/test-${i} $k > findkthlargest-${i}
  python quickselect.py sanity_check_test_cases/test-${i} $k > quickselect-${i}
  # python detselect.py sanity_check_test_cases/test-${i} $k > detselect-${i}

  # #use diff3 for comparing 3 files
  diff_output=$(diff findkthlargest-${i} quickselect-${i})
  if [ "$diff_output" ]; then
    echo "failed test number $i"
    echo $diff_output
    break
  fi
done

rm -f sanity_check_test_cases/test-*
rmdir sanity_check_test_cases

rm findkthlargest-*
rm quickselect-*
# rm detselect-*