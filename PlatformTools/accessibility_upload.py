import sys
import os
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(sys.argv[1])

engine = create_engine(os.environ["ConnectionString"])

# ",Latitude,Longitude,Mean H_s,P_0,Expected Delay"
# MeanDepth, MeanWaveHeight, MeanInstantAccessProbability, MeanExpectedDelayHours

df["MeanDepth"] = 0.0

df = df.rename(columns={
    "Mean H_s": "MeanWaveHeight",
    "P_0": "MeanInstantAccessProbability",
    "Expected Delay": "MeanExpectedDelayHours"
})

print(df.columns)

df = df[["Latitude", "Longitude", "MeanDepth", "MeanWaveHeight", "MeanInstantAccessProbability", "MeanExpectedDelayHours"]]

df.to_sql("AccessibilityRecords", engine, if_exists="append", index=False)

print("Done!")
