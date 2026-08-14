import pandas as pd
import datetime
import os

def save_log(train_losses, val_losses, batch_losses,number_of_epochs,optimiser):

    # Extracts learning rate
    lr =optimiser.param_groups[0]['lr']

    # Gets current date as string (e.g., '2026-08-15')
    date_str = datetime.date.today().strftime("%Y-%m-%d")

    # Defines folder path
    folder_path = f"../logs/loss/lr={lr}_epochs_{number_of_epochs}_{date_str}"
    os.makedirs(folder_path, exist_ok=True)
    
    # Epoch-level log
    loss_log = pd.DataFrame({
        "epoch": range(1, len(train_losses) + 1),
        "training_loss": train_losses,
        "validation_loss": val_losses
    })

    loss_log.to_csv(f"../logs/loss/lr={lr}_epochs_{number_of_epochs}_{datetime.date}/training_loss_log.csv", index=False)

    # Batch-level log
    batch_log = pd.DataFrame({
        "batch": range(1, len(batch_losses) + 1),
        "training_loss": batch_losses
    })

    batch_log.to_csv(f"../logs/loss/lr={lr}_epochs_{number_of_epochs}_{datetime.date}/batch_loss_log.csv", index=False)

    print(f"Training logs saved at {folder_path}.")