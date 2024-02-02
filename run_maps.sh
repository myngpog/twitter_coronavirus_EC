#!/bin/sh

for file in /data/Twitter\ dataset/geoTwitter20-**-**.zip; do 
    ./src/map.py --input_path="$file" &
done

echo "map.py commands for 2020 tweets are running in the background."
echo "You can disconnect, and they will continue to run."
