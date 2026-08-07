# Downloader Class to fetch datasets from Google Drive

import os
import gdown
import zipfile


class Downloader:
    def __init__(self, dataset_dir="../data", model_dir="../model"):

    ### Fields
    
        self.dataset_dir = dataset_dir
        self.model_dir = model_dir

        os.makedirs(self.dataset_dir, exist_ok=True)
        os.makedirs(self.model_dir, exist_ok=True)
        

        self.datasets = [
            {
                "id": "1v8ZKV3p6KLDMsOscVLj1Z5zgNYGJfaQp",
                "filename": "humanised_v2_first_2400.csv",
            },
            {
                "id": "1U9Lhpo2qet7dPAuswxHFGAJEggc26bR0",
                "filename": "ai_polished_v2_first_2400.csv",
            },
            {
                "id": "182-e58HGw67tacTudS7wacm6DZZCbMEZ",
                "filename": "pure_ai_v2_first_2400.csv",
            },
            {
                "id": "15BDFQcaylNmK6Uy-BaKKe__jXQ6MgdmK",
                "filename": "pure_human_v2_first_2400.csv",
            },
        ]

        self.models = [
            {
                "id": "1eU0eQVm0--OCHz_OHsM80o7Mo0E85LCg",
                "filename": "version_1.zip"
            }
        ]

    ### Methods

    def start_downloading_dataset(self):
        for data in self.datasets:
            url = f"https://drive.google.com/uc?id={data['id']}"
            file_path = f"../data/{data['filename']}"
            self.download_data_from_shared_link( url, file_path)

    def start_downloading_model(self):

            for model in self.models:
                url = f"https://drive.google.com/uc?id={model['id']}"
                file_path =f"../model/{model['filename']}"
                
                self.download_data_from_shared_link( url, file_path)

            # Extracts the ZIP file into a local directory
            with zipfile.ZipFile("../model/version_1.zip", 'r') as zip_ref:
                zip_ref.extractall("../model/")

    
    # gdown downloader helper function
    # REFERENCE: https://github.com/wkentaro/gdown

    def download_data_from_shared_link(self, url, file_path):
        # Downloads dataset from a Google Drive shared link
        gdown.download(url=url, output=file_path, fuzzy=True)