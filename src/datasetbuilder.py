# DatasetBuilder Class to reconstruct raw datasets
# REFACTOR!!: do not repeat blocks of code...

import pandas as pd


class DatasetBuilder:

    def __init__(self):
        pass

        self.raw_dataset_paths = [
            {
                "pure_human": "../data/pure_human_first_2000.csv"
            },
            {
                "pure_ai": "../data/pure_ai_first_2000.csv"
            },
            {
                "ai_polished": "../data/ai_polished_first_2000.csv"
            },
            {
                "humanised": "../data/humanised_first_2000.csv"
            },
        ]

    def build_dataset(
        self,
        pure_human_path,
        pure_ai_path,
        ai_polished_path,
        humanised_path,
    ):
        # List to gather all processed datasets
        all_datasets = []

        df_pure_human = pd.read_csv(pure_human_path)
        df_pure_ai = pd.read_csv(pure_ai_path)
        df_ai_polished = pd.read_csv(ai_polished_path)
        df_humanised = pd.read_csv(humanised_path)

        # Restructures pure human dataset with label: 0
        pure_human_dataset = pd.DataFrame(
            {
                "text": df_pure_human["generation"],
                "label": 0,
                "label_name": "pure_human",
            }
        )
        all_datasets.append(pure_human_dataset)

        # Restructures pure_ai dataset with label: 1
        pure_ai_dataset = pd.DataFrame(
            {
                "text": df_pure_ai["generation"],
                "label": 1,
                "label_name": "pure_ai",
            }
        )
        all_datasets.append(pure_ai_dataset)

        # Restructures ai_polished dataset with label: 2
        ai_polished_dataset = pd.DataFrame(
            {
                "text": df_ai_polished["rewritten_text"],
                "label": 2,
                "label_name": "human_written_ai_polished",
            }
        )
        all_datasets.append(ai_polished_dataset)

        # Restructures humanised dataset with label: 3
        humanised_dataset = pd.DataFrame(
            {
                "text": df_humanised["rewritten_text"],
                "label": 3,
                "label_name": "ai_written_humanised",
            }
        )
        all_datasets.append(humanised_dataset)


        # Merges them into a single training dataset
        final_dataset = pd.concat(all_datasets, ignore_index=True)

        return final_dataset
