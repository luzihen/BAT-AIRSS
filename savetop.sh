mkdir beststructures

#number of structures to be saved
num=10
#energytreshold to be saved
ethreshold=0.3

#look for compositions
complist=`ca -s -l | awk '{print $6}'`


for comp in $complist
do
  echo "looking at composition $comp"
  num_ethreshold=`ca -f $comp -u 0.1 -de $ethreshold -r | wc -l`
  if [ 1 -eq "$(echo "${num_ethreshold} > ${num}" | bc)" ]
    then
        reslist=`ca -f $comp -u 0.1 -de $ethreshold -r -l | awk '{print $1}'`
    else
        reslist=`ca -f $comp -u 0.1 -r -t  $num -l  | awk '{print $1}'`
  fi
  for entrytosave in $reslist
  do
      echo "saving entry - $entrytosave.res (saved in directory named beststructures)"
      cp "$entrytosave.res" beststructures/  
  done
done
