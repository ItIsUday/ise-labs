#!/bin/bash

echo -n "Enter a file name: "
read -r file_name

if [ ! -e "$file_name" ]; then
  echo "File $file_name does not exist"
  exit
fi

var=$(ls -l "$file_name" | cut -b 1)

case $var in
-)
  echo "$file_name is a regular file"
  ;;
l)
  echo "$file_name is a symbolic link file"
  ;;
d)
  echo "$file_name is a directory"
  ;;
c)
  echo "$file_name is a character device file"
  ;;
b)
  echo "$file_name is a block device file"
  ;;
*)
  echo "$file_name is unrecognizable"
  ;;
esac
