import pandas as pd
import numpy as np


def create_dataframe(list_, colnames):
    df = pd.DataFrame(np.array(list_), columns=colnames)
    return df

def save_to_csv(list_, colnames, filename):
    df = create_dataframe(list_, colnames)
    df.to_csv(filename)

