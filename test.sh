#!/bin/bash
  
begin=$(date +%s%3N)

rm log.txt

SET=$(seq 1 1)


for i in $SET
do
	num_of_p=$i
	data_json="{\"num_of_p\":\"${num_of_p}\"}"
	
	echo $data_json
	
	curl --header "Content-Type: application/json" \
		--request POST \
		--data ${data_json} \
		http://0.0.0.0:5000/log

	echo ${num_of_p}
	sleep 5
	seq 1 500 | xargs -n1 -P${num_of_p} ./run.sh $1

	sleep 5
done

end=$(date +%s%3N)

result=${end}-${begin}
echo ${result}
