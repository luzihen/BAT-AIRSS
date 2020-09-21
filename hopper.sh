#!/bin/bash -l
#$ -cwd
#$ -S /bin/bash
#$ -m n
#$ -N vasp
#$ -pe mpi 24
#$ -l h_rt=24:00:00

#$ -P Gold
#$ -A Faraday_FCAT
#$ -l mem=4G

#$ -ac allow=K
module purge
source ~/.bashrc_intel_2013

for i in ./*/
do
cd $i
if [ -f log ]
then
    if [ `tail -n 1 log | awk '{print $1}'` == 'reached' ]
    then
    echo "complete" >> mark
    pwd >> ../finished_log
    fi
else
    echo "computing" >> mark
    mpirun -np 24 vasp_std_oldintel >> log
    #cp POSCAR POSCAR.bak
    #cp CONTCAR POSCAR
    rm CHGCAR CHG DOSCAR EIGENVAL IBZKPT OSZICAR OUTCAR PCDAT PROCAR REPORT WAVECAR XDATCAR
    echo "complete" >> mark
fi
cd ..
done
