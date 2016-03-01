#!/usr/bin/env bash
pn=(6 28 496 8128 33550336 8589869056 137438691328 2305843008139952128 2658455991569831744654692615953842176 191561942608236107294793378084303638130997321548169216)

if [ -e "loop.last" ]
then
    i=`cat loop.last`
else
    i=0
fi

echo "starting test with ${i}"
while true
do
  if [ "$(python isperfect.py ${i})" == "True" ]
  then
    echo ${i} >> loop.perf
    echo ${i}
  fi
  echo ${i} > loop.last
  i=$[$i + 1]
done
