# TestEvaluator Class to calculate and log evaluation metrics on the test set

import torch
from sklearn.metrics import accuracy_score, classification_report

class TestEvaluator():
    def __init__(self, dataloader, model, device):
        self.dataloader=dataloader
        self.model=model.to(device)
        self.device=device

    def calculate_metrics(self):
        all_predictions = []
        all_true_labels = []

        self.model.eval()

        print("Evaluating the X_test dataset..")

        # 3. Turn off gradient tracking for hyper-fast inference processing
        with torch.no_grad():
            for batch in self.dataloader:
                # Send data tensors to the exact same device your model lives on
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)

                # Forward pass: Generate predictions
                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)

                # Pull the highest probability class index (0, 1, 2, or 3)
                preds = torch.argmax(outputs.logits, dim=-1)

                # Save predictions and labels back to flat CPU numpy arrays
                all_predictions.extend(preds.cpu().numpy())
                all_true_labels.extend(labels.cpu().numpy())

        # 4. Calculate the overall Accuracy score
        final_accuracy = accuracy_score(all_true_labels, all_predictions)

        # Map numeric labels back to your 4 unique string categories
        class_mapping_names = [
            "Pure Human Written (Class 0)", 
            "Pure AI Written (Class 1)", 
            "AI Polished (Class 2)", 
            "Humanised (Class 3)"
        ]

        # 5. Outputs a evaluation summary matrix report
        print(f" EVALUATION COMPLETE | OVERALL ACCURACY: {final_accuracy:.2%}")
        
        print(classification_report(all_true_labels, all_predictions, target_names=class_mapping_names, digits=4))
                  

    