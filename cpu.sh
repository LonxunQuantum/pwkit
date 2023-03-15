#!/bin/sh
#SBATCH --partition=cpu
#SBATCH --job-name=conda_pack
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --threads-per-core=1



#module load intel/2020
#source ~/.bashrc 
#conda activate base

conda pack -j 8 -n pwkit_env -o pwkit_env.tar.gz

