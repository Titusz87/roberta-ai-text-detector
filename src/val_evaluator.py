# Validation function with Early Stopping and best model saving mechanism
# REFERENCE: https://discuss.pytorch.org/t/train-py-use-early-stoping/96912/2?utm_source=chatgpt.com

import torch

def validate_model(patience, best_val_loss, model, tokenizer, val_loader,device):
    model.eval()
    
    patience_threshold = 2

    with torch.no_grad():
        epoch_val_loss = 0.0
        total_val_loss = 0.0

        for batch in val_loader:
            
            outputs = model(
                input_ids=batch['input_ids'].to(device),
                attention_mask=batch['attention_mask'].to(device),
                labels=batch['labels'].to(device)
            )

            epoch_val_loss += outputs.loss.item()

        total_val_loss=epoch_val_loss / len(val_loader)

        if (total_val_loss < best_val_loss):
            best_val_loss = total_val_loss
            patience = 0 # resets patience in case of loss improvement

            from src.save_best_model import save_model
            save_model(model, tokenizer, best_val_loss) # saves the current best model
            
        else:
            patience += 1 # increases the patience counter

        return total_val_loss, best_val_loss, patience
