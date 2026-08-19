# DatasetWrapper transforms dataset into compatible pytorch tensors

import torch

class DatasetWrapper():
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels.to_numpy() if hasattr(labels, 'to_numpy') else list(labels)

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

    def __len__(self):
        return len(self.labels)