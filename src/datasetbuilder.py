import pandas as pd


class DatasetBuilder:

    def __init__(self):
        pass

    def build_dataset(
        self, df_pure_human, df_pure_ai, df_ai_polished, df_humanised
    ):
        # List to gather all processed datasets
        all_datasets = []

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
