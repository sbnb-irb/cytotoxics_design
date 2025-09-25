#!/bin/bash

singularity exec --cleanenv --no-mount /slgpfs/projects/irb35 --no-home --nv --bind $PWD:/mnt reinvent3_signaturizer_kbest.simg python ./run_predictions.py \
    --model ./models/BXPC3.pkl \
    --kbest_reduction ./kbest_dim_reduction/BXPC3.pkl \
    --smiles_file ./example_smiles.txt \
    --output_file ./BXPC3_predictions.csv
