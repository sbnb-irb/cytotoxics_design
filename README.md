# Overview

This repository contains data and scripts from the paper *AI-based design of cell-specific small molecule cytotoxics* [add citation]

---

# Folder Structure

## 1. `drug_screening_data.xlsx`

Contains all the experimental screening data. The different tabs correspond to:

- `HTS`: High-throughput screening results (11,053 cpds, 1 replicate).
- `Confirmation experiment of HTS hits`: Confirmed hits from HTS (751 cpds, 2 replicates).
- `Final training dataset`: Aggregation of the 3 replicates from the HTS (1) and confirmation (2) experiments as mean of the 2 closest reps (751 cpds).
- `Validation of prediction models`: Experimental validation of the cytotoxicity prediction models (320 cpds, 2 replicates).
- `Validation of generated molecules at 1 and 10 uM`: Validation at 1 and 10uM of the initial candidates from the 'generation' approach.
- `Validation of prediction-only molecules at 1 and 10 uM`: Validation at 1 and 10uM of the initial candidates from the 'predictions-only' approach.
- `DR generated molecules`: Dose-response measurements for the final candidates from the generated approach.
- `DR prediction only molecules`: Dose-response measurements for final candidates for the 'prediction-only' approach.
- `MTT 12 drugs DrugCell`: Dose-response measurements obtained via MTT assay for 12 selected compounds from DrugCell (Extended Data Fig. 2b).

---

## 2. `high-scoring generated molecules.xlsx`

Contains all the high-scoring, generated molecules for all the exercises.

---

## 3. `cytotoxicity_prediction_models/`

Contains the models used for cytotoxicity prediction and examples of how to use them to predict cytotoxicity for new SMILES.

- `example_smiles.txt`: Example compounds in SMILES format for testing the prediction scripts.
- `example_usage.sh`: Example shell script showing how to run predictions with the models.
- `kbest_dim_reduction/`: Pickle files containing the sckit objects needed to reduce the CC_GLOBAL descriptors (the models take the reduced descriptors as input).
- `models/`: Pickle files with trained prediction models for each cell line.
- `predict_IRB_library.py`: Python script to run predictions on new compounds.

---

## 4. `RNAseq/`

Contains RNA sequencing data and processed expression matrices.

- `cnts.multi.xlsx`: Raw counts for multiple samples.
- `geneinfo.xlsx`: Gene annotation information.
- `raw_count_processed_names_mean_expression.xlsx`: Processed counts with mean expression per gene.
- `sampleinfo.xlsx`: Metadata about the RNA-seq samples.
