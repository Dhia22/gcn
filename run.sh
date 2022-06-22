#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --mem=20g
set -x
source activate env_YOLACT
export CUDA_VISIBLE_DEVICES=$SLURM_JOB_GPUS
python train.py --config=yolact_resnet50_generated_dwg_config &> log_yolact.txt
set +x
