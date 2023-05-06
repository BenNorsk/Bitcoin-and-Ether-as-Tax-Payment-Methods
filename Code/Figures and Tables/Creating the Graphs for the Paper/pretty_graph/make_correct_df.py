import pandas as pd
import os
import sys

cutoff = 0

# Iterate through all folder in the "A1.0" directory
for folder in os.listdir("A1.0"):
    # get the foldername
    foldername = folder
    # get the weights for the cufoff
    weights = pd.read_csv("A1.0/" + foldername + f'/{cutoff}_weights.csv', index_col=0)
    # get the data for y and y_star
    data = pd.read_csv("A1.0/" + foldername + f'/{cutoff}_synth_{foldername}.csv', index_col=0)
    

