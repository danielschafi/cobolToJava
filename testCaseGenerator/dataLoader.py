import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()
"""
Loads the data and prepares it for further processing
"""


def loadData() -> pd.DataFrame:
    df = pd.read_csv(os.environ.get("DATASET_URL"))
    cobol_code_examples = df["source"]
    return cobol_code_examples
    
    
if __name__ == "__main__":
    loadData()