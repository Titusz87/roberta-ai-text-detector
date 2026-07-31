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
                "id": "16hDeETXMq4-o67YSqguDk6OC3VvXW7U7",
                "filename": "ai_written_humanised_v3_last2500.csv",
            },
            {
                "id": "1cAL9qHhyYIVnR0kxMBlzRFFyrZqiCf6O",
                "filename": "HUMAN_written_then_AI_polished_v3_last2500.csv",
            },
            {
                "id": "1LlTrJ6wdRkctvpT21O_XkNTfrHOBhX6L",
                "filename": "ai_generated_v2_last2500.csv",
            },
            {
                "id": "1Meg3aFojjCGefepim0zVsArmze_5ttGy",
                "filename": "human_written_v2_last2500.csv",
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