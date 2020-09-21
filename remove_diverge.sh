mkdir garbage

#look for compositions
complist=`ca -s -l | awk '{print $6}'`
threshold=1.0

for comp in $complist
do

echo "looking at composition $comp"

seconde=`ca -f "$comp" -r | awk '{print $4}' | head -n 2 | tail -n 1`
   
while [ 1 -eq "$(echo "${seconde} > ${threshold}" | bc)" ]
do 
    entrytoremove=`ca -f $comp -r -l| awk '{print $1}' | head -n 1`
    echo "removing inappropriate entry - $entrytoremove.res (saved in directory named garbage)"
    mv "$entrytoremove.res" garbage
    seconde=`ca -f "$comp" -r | awk '{print $4}' | head -n 2 | tail -n 1`
done

done


