#!/usr/bin/env bash
pn=(6 28 496 8128 33550336 8589869056 137438691328 2305843008139952128 2658455991569831744654692615953842176 191561942608236107294793378084303638130997321548169216)

pn=(137438691328 2305843008139952128)

echo ":: rich:"
for i in "${pn[@]}"
do
  echo ${i}
  time python ../perfectnumber/is_perfect.py ${i}
  echo "------------"
done

echo ":: v2:"
for i in "${pn[@]}"
do
  echo ${i}
  time python a.py v2 ${i}
  echo "------------"
done

echo ":: v3:"
for i in "${pn[@]}"
do
  echo ${i}
  time python a.py v3 ${i}
  echo "------------"
done

echo ":: v4:"
for i in "${pn[@]}"
do
  echo ${i}
  time python a.py v4 ${i}
  echo "------------"
done
