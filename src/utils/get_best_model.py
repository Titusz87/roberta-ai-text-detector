# Helper function to return the model path with the lowest loss
#REFERENCE: https://stackoverflow.com/questions/59122657/is-there-a-way-in-python-to-find-a-file-with-the-smallest-number-in-its-name

import os

def find_best_model(model_root_path="../model/"):

    # Extracts the loss string, converts it to a float, and stores the minimum score
    best_folder = min(model_root_path, key=lambda f: float(f.split("_loss_")[-1].replace("/", "")))
    
    # Builds the best model path string
    best_model_path = os.path.join(model_root_path, best_folder) + "/"

    return best_model_path