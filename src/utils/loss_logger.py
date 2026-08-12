import pandas as pd
import datetime
import os

def save_log(train_losses, val_losses, batch_losses,number_of_epochs,learning_rate):

    os.makedirs(self.dataset_dir, exist_ok=True)
    
    # Epoch-level log
    loss_log = pd.DataFrame({
        "epoch": range(1, len(train_losses) + 1),
        "training_loss": train_losses,
        "validation_loss": val_losses
    })

    loss_log.to_csv(f"../data/loss/lr={learning_rate}_epochs_{number_of_epochs}_{datetime.date}/training_loss_log.csv", index=False)

    # Batch-level log
    batch_log = pd.DataFrame({
        "batch": range(1, len(batch_losses) + 1),
        "training_loss": batch_losses
    })

    batch_log.to_csv(f"../data/loss/lr={learning_rate}_epochs_{number_of_epochs}_{datetime.date}/batch_loss_log.csv", index=False)

    print("Training logs saved at .")