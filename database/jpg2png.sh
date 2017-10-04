#!/bin/sh
# ./jpg2png.sh Yelmo/*.jpg
for f in $* ;do
 if echo "$f" | grep -i "jpg$" > /dev/null ; then
   png=`echo "$f" | sed 's/jpg$/png/i'`
   echo "converting  $f to $png ..."
   convert  $f  -colorspace Gray   $png
   #rm -f $f
 else
   echo echo "$f is not a jpg file, ignored"
 fi
done
