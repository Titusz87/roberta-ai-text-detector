from src.utils.version_number_generator import get_next_version_number

def save_model(model, tokenizer, val_loss):
    current_version_number = get_next_version_number()  # gets current version number integer
    path = f"model_version_#{current_version_number}_loss={val_loss}"       # sets model path

    # Saves model and tokeniser configurations
    model.save_pretrained(f"../model/{path}/")
    tokenizer.save_pretrained(f"../model/{path}/")
    print(f"A new best model is saved with loss: {val_loss}, located at 'model/{path}/'.")