import argparse
import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "nba-player.csv"
with open(os.path.join("..", "data", filename), "rb") as f:
    ratings = pd.read_csv(f,names=("player","salary","team","position","team-agaisnt","ceiling","floor","points"))
print(ratings)