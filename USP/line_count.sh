#!/bin/bash

echo -n "Enter a file name: "
read -r file_name

if [ ! -e "$file_name" ]; then
  echo "File $file_name does not exist"
  exit
fi

line_count=$(grep "" -c "$file_name")
echo "There are $line_count lines in $file_name"
