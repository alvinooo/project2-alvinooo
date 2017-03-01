#!/bin/bash

# ./runBlockServer.sh config.txt &
# ./runMetaServer.sh config.txt 1 &

# until [[ $(ps | grep Server | grep -v 'grep' | cut -d' ' -f2 | wc -l) -ne 0 ]]; do
# 	sleep 1
# done

# ./runClient.sh config.txt test_upload upload test0.txt
# ./runClient.sh config.txt test_download download test0.txt

# UPLOAD_LENGTH=$(wc -c test_upload/test0.txt | awk {'print $1'})
# DOWNLOAD_LENGTH=$(wc -c test_download/test0.txt | awk {'print $1'})
# DIFF=$(diff test_upload/test0.txt test_download/test0.txt)

# if [ $UPLOAD_LENGTH -eq $DOWNLOAD_LENGTH ] && [ -z $DIFF ]; then
# 	echo "Upload + download same file...PASSED"
# fi
# rm test_download/test0.txt

# for PID in $(ps | grep Server | grep -v 'grep' | cut -d' ' -f2)
# do
# 	kill -TERM $PID
# done

# # Overlapping uploads
# ./runClient.sh config.txt test_upload upload part1.txt
# ./runClient.sh config.txt test_upload upload part2.txt
# ./runClient.sh config.txt test_upload upload part1plus2.txt

# ./runClient.sh config.txt test_upload upload part1plus2.txt
# ./runClient.sh config.txt test_upload upload part1.txt
# ./runClient.sh config.txt test_upload upload part2.txt

# # Overlapping downloads
# ./runClient.sh config.txt test_upload upload part1plus2.txt
# rm test_download/*.txt

# printf "3333\n1111\n" > test_download/exist_1.txt
# ./runClient.sh config.txt test_download download part1plus2.txt
# rm test_download/*.txt

# printf "2222\n1111\n" > test_download/exist_all.txt
# ./runClient.sh config.txt test_download download part1plus2.txt
# rm test_download/*.txt

# Versioned downloads

echo "Downloading nonexistent file"
./runClient.sh config.txt test_upload upload part1.txt
./runClient.sh config.txt test_download download part1.txt

echo "Downloading a newer version"
sleep 1
touch test_upload/part1.txt
./runClient.sh config.txt test_upload upload part1.txt
./runClient.sh config.txt test_download download part1.txt

echo "Downloading an older version"
sleep 1
touch test_download/part1.txt
./runClient.sh config.txt test_upload upload part1.txt
./runClient.sh config.txt test_download download part1.txt

rm test_download/*.txt