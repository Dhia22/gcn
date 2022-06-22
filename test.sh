#!/bin/bash
#SBATCH --gres=gpu:1
#SBATCH --mem=20g
set -x
source activate env_YOLACT
export CUDA_VISIBLE_DEVICES=$SLURM_JOB_GPUS
python eval.py --trained_model=weights/yolact_plus_resnet50_generated_dwg_795_140000.pth --config yolact_resnet50_generated_dwg_config --score_threshold=0.1 --top_k=30 --image=data/rtest.png &> log_yolactTest.txt
set +x
