#!/bin/bash


function compile() {
dist=./uic
src=./ui

rm -rf $dist

mkdir $dist

for file in $src/*.ui; do
  name=$(basename $file .ui)
  file_dist="$dist/$name.py"
  echo "Compile $file to $file_dist"
  pyuic5 -o $file_dist $file
done;
}

compile

if [ "$1" == '--watch' ]; then
  echo "Start watching"
  while true; do
      sleep 5
      compile
  done
fi