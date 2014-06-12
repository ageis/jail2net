#!/bin/bash
data=$1
str="${data%.wav}"
str2="${str##*/}"
str3="$str2.mp3"
str4="${data##*/}"
dest=$1
msg=`exiftool $data`
tmp=/var/asterisk

cp $data $tmp
cd $tmp
lame -m m -b 128 $data $str3
python /var/asterisk/post.py $str3
rm $data
rm $str4
