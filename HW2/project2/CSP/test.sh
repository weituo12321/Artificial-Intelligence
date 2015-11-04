#!/bin/bash
# My first script

for c in {0..81}
do
  python sudokuGenerator.py $c
  python sudokuSolver.py fancy
  python sudokuChecker.py | grep 'solution checked.' &> /dev/null
  if [ $? != 0 ]; then
     echo 'error'
     break
  fi
done
