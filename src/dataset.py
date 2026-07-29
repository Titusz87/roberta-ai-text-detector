def find_cat_dog_lion_tiger_folders(start_path="."):
    start = Path(start_path).resolve()

    # Initializes variables as None
    cats_dir = dogs_dir = lion_dir = tiger_dir = None

    print("### Searching for dataset folders... ###")

    # Searching starts within current directory for the 'train' folder
    for path in start.rglob("train"):
        # Looks for all subfolders in the found 'train' directory
        cat = path / "cats"
        dog = path / "dogs"
        lion = path / "lion"
        tiger = path / "tiger"

        # Returns dataset paths if valid structure is found
        if cat.exists() and dog.exists() and lion.exists() and tiger.exists():
            print("### All training folders found ###")
            # Explicitly return the four paths here
            return lion, tiger, cat, dog

    # If the loop finishes without returning, the folders weren't found
    print("### Dataset folders not found. ###")
    raise FileNotFoundError("Could not locate cats, dogs, lion, and tiger folders under a 'train' directory.")


# Dataset Download Function
import os
import gdown

os.makedirs("../data", exist_ok=True)

def download_data_from_shared_link(url, file_name):
    # Downloads dataset from a Google Drive shared link
    gdown.download(url=url, output=file_name)
