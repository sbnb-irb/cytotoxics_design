import pickle, sys
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn.feature_selection import SelectKBest
from signaturizer import Signaturizer
from sklearn.metrics import average_precision_score, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
import logging
import argparse
import os
os.environ["TFHUB_CACHE_DIR"] = "/aloy/scratch/grojas/tf_tmp"

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format for log messages
    datefmt="%Y-%m-%d %H:%M:%S",  # Date and time format
)

def parse_args():
    parser = argparse.ArgumentParser(description="Run cytotoxicity prediction model.")
    parser.add_argument("--model", type=str, required=True, help="Model name to use.")
    parser.add_argument("--kbest_reduction", type=str, default=None, help="Number of top features to keep (optional).")
    parser.add_argument("--smiles_file", type=str, required=True, help="Input SMILES file path.")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save the output file.")
    return parser.parse_args()

# Parse command-line arguments
args = parse_args()
model_file = args.model
kbest_file = args.kbest_reduction
smiles_file = args.smiles_file
output_file = args.output_file

# Load predictor and K-best feature extractor
logging.info("Loading dim reducer from %s" % kbest_file)
with open(kbest_file, "rb") as f:
    kbest = pickle.load(f)

logging.info("Loading model from %s" % model_file)
with open(model_file, "rb") as f:
    model = pickle.load(f)

# Load smiles to predict
logging.info("Read SMILES file")
with open(smiles_file, "r") as f:
    smiles = [line.strip() for line in f if line.strip()]

logging.info("Signaturize compounds")
sign = Signaturizer("GLOBAL")
X = sign.predict(smiles).signature
X = kbest.transform(X)

# Make predictions
logging.info("Make predictions")
probabilities = model.predict_proba(X)[:, 1]

# Save results
results_df = pd.DataFrame({"SMILES": smiles, "Probability": probabilities})
results_df.to_csv(output_file, index=False)

logging.info("FINISHED")
