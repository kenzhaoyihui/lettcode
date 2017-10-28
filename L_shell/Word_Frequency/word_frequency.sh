# Read from the file words.txt and output the word frequency list to stdout.
# 1. cat words.txt |sed 's/[,.:;/!?]/ /g'|awk '{for (i=1;i<=NF;i++) array[$i]++;}END{for(i in array) print i, array[i]}' |sort -k 2 -n -r

# 2. egrep -o "\b[[:alpha:]]+\b" words.txt |awk '{count[$0]++} END{for(i in count){printf("%s %d\n",i,count[i]);}}' |sort -k 2 -n -r

# 3. sed 's/[,.:;/!?]/ /g' words.txt|awk '{for(i=1;i<=NF;i++) array[$i]++;}END{for(i in array) print i, array[i]}' |sort -k 2 -n -r

4. awk 'BEGIN{RS="[,.:;/!?]"}{for(i=1;i<=NF;i++)array[$i]++;}END{for(i in array) print i, array[i]}' words.txt |sort -k 2 -n -r
