# Downloader Class to fetch datasets, models and loss logs from Google Drive

import os
import gdown
import zipfile


class Downloader:
    def __init__(self, dataset_dir="../data", model_dir="../model", loss_dir="../logs/loss" ):

    ### Fields
    
        self.dataset_dir = dataset_dir
        self.model_dir = model_dir
        self.loss_dir = loss_dir

        os.makedirs(self.dataset_dir, exist_ok=True)
        os.makedirs(self.model_dir, exist_ok=True)
        os.makedirs(self.loss_dir, exist_ok=True)
        

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
                "id": "1MatKPKXHSUa8RbryhmR43nUH6e6wgmZk",      # Current best model
                "filename": "model_version_#5_loss_0.03069869413933096.zip"
            }
        ]

        self.losses = [
            {
                "id": "17Tpzq9fjzB-sTx1kA6QJKHbGLFwxi1U3",   
                "filename": "lr=2e-5_epochs_10.zip"  # current best model's loss logs
            },
            {
                "id": "18BinGfAgLjSfYvUHso-awCM6YsailVNZ",
                "filename": "lr=2e-5_epochs=5.zip",
            },
            {
                "id": "1wKWPzQkYxteqnjpZx6aHD3DP_Lz4iruM",
                "filename": "lr=5e-5_epochs=5.zip",
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
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall("../model/")

    def start_downloading_logs(self):
            for loss in self.losses:
                url = f"https://drive.google.com/uc?id={loss['id']}"
                file_path = f"../logs/loss/{loss['filename']}"

                self.download_data_from_shared_link( url, file_path)

                # Extracts the ZIP file into a local directory
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall("../logs/loss/")

    
    # gdown downloader helper function
    # REFERENCE: https://github.com/wkentaro/gdown

    def download_data_from_shared_link(self, url, file_path):
        # Downloads dataset from a Google Drive shared link
        gdown.download(url=url, output=file_path, fuzzy=True)