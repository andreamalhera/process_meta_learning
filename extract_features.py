import os
import pandas as pd
from tqdm import tqdm
from meta_feature_extraction import pipeline, sort_files


print("Extracting meta-features")
combined_features = []
for file in tqdm(sort_files(os.listdir(event_logs_path))):
    combined_features.append(pipeline(event_logs_path, file))

with open("meta_feature_extraction/column_names.txt") as f:
    columns = f.readlines()
columns = [x.strip() for x in columns]

print("Saving meta-features")
pd.DataFrame(combined_features, columns=columns).to_csv("log_features.csv", index=False)
