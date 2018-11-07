#! /bin/bash

while getopts s:d: option
do
case "${option}"
in
s) SRC=${OPTARG};;
d) DEST=${OPTARG};;
esac
done

FAIL_FLAG=false
function failed_exit() {
    echo "USAGE: stream_recorder -s [SRC] -d [DEST]"
    echo "received SRC: $SRC"
    echo "recieved DEST: $DEST"
    exit
}

# Simple Verification: SRC is not empty
if [ -z "$SRC" ]; then
echo "ERROR: Source (-s) must be a valid audio source."
FAIL_FLAG=true
fi

# Simple Verification: DEST is not empty
if [ -z "$DEST" ]; then
echo "ERROR: Destination (-d) must be a valid filepath."
FAIL_FLAG=true
fi

if $FAIL_FLAG ; then
    failed_exit
fi



echo "Beginning execution!"

#ffmpeg -i http://relay.broadcastify.com/76gzvyqjm93hfrk.mp3 -c copy out.mp3

# https://stackoverflow.com/questions/36074224/how-to-split-video-or-audio-by-silent-parts  
ffmpeg -i $SRC -c copy $DEST  


