#!/bin/bash

rm test_download/*.txt
./runClient.sh config.txt test_upload upload part1plus2.txt

echo "Overlapping downloads"

echo "Overlapping by 1"
echo "Expected 1"
printf "3333\n1111\n" > test_download/exist_1.txt
./runClient.sh config.txt test_download download part1plus2.txt
rm test_download/*.txt

echo "Overlapping by all"
echo "Expected 0"
printf "2222\n1111\n" > test_download/exist_all.txt
./runClient.sh config.txt test_download download part1plus2.txt
rm test_download/*.txt

# Versioned downloads
echo "Downloading nonexistent file"
echo "Expected ERROR"
./runClient.sh config.txt test_upload delete part1.txt
./runClient.sh config.txt test_download download part1.txt

echo "Downloading a newer version"
echo "Expected OK"
sleep 1
touch test_upload/part1.txt
./runClient.sh config.txt test_upload upload part1.txt
./runClient.sh config.txt test_download download part1.txt

echo "Downloading an older version"
echo "Expected OK"
sleep 1
touch test_download/part1.txt
./runClient.sh config.txt test_upload upload part1.txt
./runClient.sh config.txt test_download download part1.txt

rm test_download/*.txt