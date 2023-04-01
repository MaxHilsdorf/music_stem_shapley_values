import pandas as pd
import numpy as np
from music_shapley import MusicShapley

# Read data
df = pd.read_excel("../analysis_results/classifier_outputs.xlsx", dtype={"track": str})

# Instantiate shapley computer
stem_names = ["vocals", "eguitar", "drums", "bass", "piano"]
MuSh = MusicShapley(df, "027223", "track", "coalition", "genre1_score", stem_names)

# Print shapley values for each instrument
for stem in stem_names:
    print(stem, MuSh.get_shapley_val(stem))