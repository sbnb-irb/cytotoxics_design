# Overview

This repository contains data and scripts from the paper *AI-based design of cell-specific small molecule cytotoxics* [add citation]

---

# Folder Structure

## 1. `screening_data/`

Contains the experimental screening data.

### a) `HTS/`
- `HTS.csv`: High-throughput screening results (11,053 cpds).
- `HTS_hits_confirmation.csv`: Confirmed hits from HTS (392 cpds).
- `processed_HTS_hits_confirmation.csv`: Aggrefation of the 3 replicates from the HTS (1) and confirmation (2) experiments as mean of the 2 closest reps (392 cpds).

### b) `Validation of prediction models/`
- Experimental validation of the cytotoxicity prediction models.
  
### c) `Validation of generation vs library prediction strategies/`
- Validation at 1 and 10uM of the initial candidates from the 'generation' and 'prediction-only' approaches.

### d) `Dose-Response/`
- `DR_data_IRB_predicted_molecules.csv`: Dose-response measurements for final candidates for the 'prediction-only' approach.
- `DR_generated_molecules.csv`: Dose-response measurements for the final candidates from the generated approach.
- 
---

## 2. `cytotoxicity_prediction_models/`

Contains the models used for cytotoxicity prediction and examples of how to use them to predict cytotoxicity for new SMILES.

- `example_smiles.txt`: Example compounds in SMILES format for testing the prediction scripts.
- `example_usage.sh`: Example shell script showing how to run predictions with the models.
- `kbest_dim_reduction/`: Pickle files containing the sckit objects needed to reduce the CC_GLOBAL descriptors (the models take the reduced descriptors as input).
- `models/`: Pickle files with trained prediction models for each cell line.
- `predict_IRB_library.py`: Python script to run predictions on new compounds.
  
---

## 3. `high_scoring_generated_molecules/`

Contains all the high-scoring, generated molecules for all the exercises.

---

## 4. `RNAseq/`

Contains RNA sequencing data and processed expression matrices.

- `cnts.multi.xlsx`: Raw counts for multiple samples.
- `geneinfo.xlsx`: Gene annotation information.
- `raw_count_processed_names_mean_expression.xlsx`: Processed counts with mean expression per gene.
- `sampleinfo.xlsx`: Metadata about the RNA-seq samples.
