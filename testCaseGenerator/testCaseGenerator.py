# Environment Variables
import os
from dotenv import load_dotenv
load_dotenv()

# Logging Setup
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log", level=logging.INFO)

# Other Imports
from datasets import load_dataset
import pandas as pd


from utils.llm import LLM


class TestCaseGenerator():
    """
    Class for generating the test caes from the cobol files in cobol and java
    Saving all the info in a JSON file
    """
    def __init__(self):    
        self.output_file: str = os.getenv("TEST_CASE_OUTPUT")
        
        self.dataset = pd.read_csv(os.environ.get("DATASET_URL"))["source"] 
        self.llm = LLM()
        self.until =4
    
    
    
    def run(self):
        for i, cob_src in enumerate(self.dataset):
            if i==self.until:
                print(cob_src)
            elif i>self.until:
                break
            
    # def _process():
    #     pass
        
        
    
    
    
    
    
    
if __name__ == "__main__":
    tcg = TestCaseGenerator()
   
    tcg.run()
    

    
    