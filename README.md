# Overview

This repository contains data and scripts from the paper *Phenotypic AI-based design of cell-specific small molecule cytotoxics*.

**Citation**:  Phenotypic AI-based design of cell-specific small molecule cytotoxics
Gema Rojas-Granado, Marta Sanchez-Soto, Jesus Calahorra, Maria Caballero, Israel Ramos, Martino Bertoni, Patrick Aloy
bioRxiv 2025.10.15.682546; doi: <https://doi.org/10.1101/2025.10.15.682546> 

---

# Folder Structure

## 1. `drug screening data/`

Contains all the experimental screening data. The different files correspond to:

- `HTS_and_confirmation.xlsx`: High-throughput screening results (11,053 cpds, 1 replicate) and confirmed hits from HTS (751 cpds, 2 replicates). Also incnludes the final training dataset (mean 2 closest replicates from HTS and confirmation) and a control screening of 320 on HEK293.
- `Validation of prediction models.xlsx`: Experimental validation of the cytotoxicity prediction models (320 cpds, 2 replicates).
- `Validation of generated molecules vs prediction only approach.xlsx`: Validation at 1 and 10uM of the initial candidates from the 'generation' and 'predictions only' approach, and posterior dose-response evaluation of the hits.
- `MTT 12 drugs DrugCell`: Dose-response measurements obtained via MTT assay for 12 selected compounds from DrugCell.

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
