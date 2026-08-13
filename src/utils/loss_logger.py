import pandas as pd
import datetime

def save_log(train_losses, val_losses, batch_losses,number_of_epochs,optimiser):
    
    # Epoch-level log
    loss_log = pd.DataFrame({
        "epoch": range(1, len(train_losses) + 1),
        "training_loss": train_losses,
        "validation_loss": val_losses
    })

    loss_log.to_csv(f"../logs/loss/lr={optimiser.param_groups[0]['lr']}_epochs_{number_of_epochs}_{datetime.date}/training_loss_log.csv", index=False)

    # Batch-level log
    batch_log = pd.DataFrame({
        "batch": range(1, len(batch_losses) + 1),
        "training_loss": batch_losses
    })

    batch_log.to_csv(f"../logs/loss/lr={optimiser.param_groups[0]['lr']}_epochs_{number_of_epochs}_{datetime.date}/batch_loss_log.csv", index=False)

    print("Training logs saved at /logs/loss/.")