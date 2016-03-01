#!/usr/bin/env bash
pn=(6 28 496 8128 33550336 8589869056 137438691328 2305843008139952128 2658455991569831744654692615953842176 191561942608236107294793378084303638130997321548169216)

pn=(137438691328 2305843008139952128)
tf="%E"
echo ":: nobler:"
for i in "${pn[@]}"
do
  echo "==:: ${i}"
  /usr/bin/time -f ${tf} python ../perfectnumber/is_perfect.py ${i}
done

echo ":: napalm:"
for i in "${pn[@]}"
do
  echo "==:: ${i}"
  /usr/bin/time -f ${tf} python isperfect.py ${i}
done
