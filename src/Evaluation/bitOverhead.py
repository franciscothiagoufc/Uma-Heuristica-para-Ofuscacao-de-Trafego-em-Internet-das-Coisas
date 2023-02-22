import pandas as pd
import numpy as np

if __name__ == "__main__":
    GT = "../../Data/Processed/groundTruthFeatures/"
    PD = "../../Data/Processed/paddingFeatures/2/"
    filenames = ['16-09-25.csv','16-09-26.csv','16-09-27.csv','16-09-28.csv','16-09-29.csv','16-09-30.csv','16-10-01.csv','16-10-02.csv','16-10-03.csv','16-10-04.csv','16-10-05.csv','16-10-06.csv','16-10-07.csv','16-10-08.csv','16-10-09.csv','16-10-10.csv','16-10-11.csv','16-10-12.csv']
    original = 0
    padding = 0
    for file in filenames:
        print(file)
        df = pd.read_csv(GT+file+"_features.csv")
        original = original + df["total"].sum()
        df = pd.read_csv(PD+file+".csv_features.csv")
        padding = padding + df["total"].sum()
    print(padding/original)
