#!/bin/bash

while true; do
  rm -rf ui
  mkdir ui
  for file in ./uic/*.ui; do
    name=$(basename $file .ui)
    dist="./ui/$name.py"
    echo "Compile $file to $dist"
    pyuic5 -o $dist $file
  done;
  sleep 2
done