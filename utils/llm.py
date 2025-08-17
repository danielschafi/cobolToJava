# Environment Variables
import os
from dotenv import load_dotenv
load_dotenv()

# Logging Setup
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename="app.log", level=logging.info)

# Other Imports
from transformers import AutoModelForCausalLM, AutoTokenizer



class LLM():
    def __init__(self):
        self.model_name = os.getenv("MODEL_NAME")
        
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype="auto",
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)


    def predict(self,
                prompt:str, 
                system_prompt:str = "You are a helpful assistant."):
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

        generated_ids = self.model.generate(
            **model_inputs,
            # max_new_tokens=512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        
        if not response:
            logging.warning("response from LLM is empty!")
            
        return response