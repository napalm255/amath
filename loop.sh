#!/usr/bin/env bash
pn=(6 28 496 8128 33550336 8589869056 137438691328 2305843008139952128 2658455991569831744654692615953842176 191561942608236107294793378084303638130997321548169216)

pn=(137438691328 2305843008139952128)

echo ":: v2 (main):"
i=0
while true
do
  echo ${i} $(python a.py v2 ${i})
  i=$[$i + 1]
done
