#!/bin/bash

###
pre='@images/pic_'
num=$1
post='.jpeg'

img_path="${pre}${num}${post}"

###

begin=$(date +%s%3N)
##
curl -v -F file=${img_path} 'http://0.0.0.0:5000/upload_jpg'
end=$(date +%s%3N)

result="${begin} ${end}"

echo ${result} >> log.txt

