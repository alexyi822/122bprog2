#!/bin/bash

TIMEFORMAT=%R

algorithm=$1
numFiles=$2
numInt=$3

program=$algorithm.py

echo "Sample Number","Language","Time (seconds)","Number of Compares" >> $algorithm-stats-$numInt.csv

k=$(($RANDOM % $numInt))

for i in $(seq $numFiles)
do
  touch input-${i}
  for j in $(seq $numInt)
  do
    echo $RANDOM >> input-${i}
  done
  python $program input-${i} $k > stats_output-${i}
  

  NUMCOMP=$(grep Comp stats_output-${i} | grep -o -E '[0-9]+')
  RUNTIME=$(grep Tim stats_output-${i} | grep -o -E '[0-9]+.[0-9]+')
  # RUNTIME=$( { time python $program input-${i} $k ; } 2>&1 )

  echo -e "\n${i}","Python","$RUNTIME","$NUMCOMP" >> $algorithm.csv

done

rm input-*
rm stats_output-*