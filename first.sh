#!/bin/bash
  
begin=$(date +%s%3N)

seq 1 100 | xargs -n1 -P${num_of_p} ./run.sh $1


end=$(date +%s%3N)

result=${end}-${begin}
echo ${result}
