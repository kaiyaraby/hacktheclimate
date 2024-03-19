import sys
import os
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(sys.argv[1])

engine = create_engine(os.environ["ConnectionString"])

# ",Latitude,Longitude,Mean H_s,P_0,Expected Delay"
# MeanDepth, MeanWaveHeight, MeanInstantAccessProbability, MeanExpectedDelayHours

df = df.rename(columns={
    "O&M Cost (£/kW/Year)": "MeanCostPerKiloWatt",
    "Downtime": "MeanDowntime",
    "Availability": "MeanAvailability",
    "Annual Energy Yield (GWh)": "MeanAnnualExpectedPower",
})

print(df.columns)

df = df[["Latitude", "Longitude", "MeanCostPerKiloWatt", "MeanDowntime", "MeanAvailability", "MeanAnnualExpectedPower"]]

df.to_sql("TurbineRecords", engine, if_exists="append", index=False)

print("Done!")
