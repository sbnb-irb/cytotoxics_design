#!/bin/bash

singularity exec --cleanenv --contain --nv --bind $PWD:/repo reinvent3_signaturizer_kbest.simg python /repo/run_predictions.py \
    --model /repo/models/BXPC3.p \
    --kbest_reduction /repo/kbest_dim_reduction/BXPC3.p \
    --smiles_file /repo/example_smiles.txt \
    --output_file /repo/BXPC3_predictions.csv
