# Downloader Class to fetch datasets from Google Drive

import os
import gdown


class DatasetDownloader:
    def __init__(self, data_dir="../data"):

    ### Fields
    
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)

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

    ### Methods

    def start_downloading_dataset(self):
        for data in self.datasets:
            url = f"https://drive.google.com/uc?id={data['id']}"
            file_path = f"../data/{data['filename']}"
            self.download_data_from_shared_link( url, file_path)

    
    # gdown downloader helper function
    # REFERENCE:

    def download_data_from_shared_link(self, url, file_path):
        # Downloads dataset from a Google Drive shared link
        gdown.download(url=url, output=file_path, fuzzy=True)