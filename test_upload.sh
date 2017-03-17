#!/bin/bash

echo "Uploading duplicate content"
echo "11, 0"
./runClient.sh config.txt test_upload upload test0.txt
./runClient.sh config.txt test_upload upload test0dup.txt

echo "Uploading parts before whole"
echo "1, 1, 0"
./runClient.sh config.txt test_upload upload part1.txt
./runClient.sh config.txt test_upload upload part2.txt
./runClient.sh config.txt test_upload upload part1plus2.txt

echo "Uploading whole before parts"
echo "2, 0, 0"
./runClient.sh config.txt test_upload upload part3plus4.txt
./runClient.sh config.txt test_upload upload part3.txt
./runClient.sh config.txt test_upload upload part4.txt

echo "Uploading part-whole-part"
echo "1, 1, 0"
./runClient.sh config.txt test_upload upload part5.txt
./runClient.sh config.txt test_upload upload part5plus6.txt
./runClient.sh config.txt test_upload upload part6.txt