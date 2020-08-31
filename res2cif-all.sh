for i in *.res
do
cabal res cif < $i > ${i%.*}.cif
done
