# Helper function to return the model path with the lowest loss
#REFERENCE: https://stackoverflow.com/questions/59122657/is-there-a-way-in-python-to-find-a-file-with-the-smallest-number-in-its-name

import os

def find_best_model(model_root_path="../model/"):

    best_folder = None
    smallest_loss = float('inf')

    for folder_name in os.listdir(model_root_path):
        loss_value = float(folder_name.split("_loss_")[-1].replace("/", ""))

        if loss_value < smallest_loss:
                    smallest_loss = loss_value
                    best_folder = folder_name

    
    # Builds the best model path string
    best_model_path = os.path.join(model_root_path, best_folder) + "/"

    return best_model_path