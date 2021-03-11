#!/bin/bash
  
begin=$(date +%s%3N)

rm log.txt

seq 1 5 | xargs -n1 -P30 ./run.sh $1

end=$(date +%s%3N)

result=${end}-${begin}
echo ${result}
