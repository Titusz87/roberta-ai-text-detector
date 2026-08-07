# Counts existing children in the model directory and returns the next sequential integer.

import os

def get_next_version_number(model_root_path="../model/"):
  
    os.makedirs(model_root_path, exist_ok=True)
    return len(os.listdir(model_root_path)) + 1
