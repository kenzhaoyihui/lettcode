array=()

while read -a columns;do
  #length=${#columns[@]} or ${#column[*]}
         for ((i=0;i<${#columns[@]};i++));do
  array[i]="${array[i]} ${columns[i]}"
  done
done < file.txt
  
for((i=0;i<${#array[@]};i++));do
         echo ${array[i]}
done

