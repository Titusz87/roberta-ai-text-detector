# REFERENCE: https://docs.pytorch.org/docs/2.13/generated/torch.where.html

import torch

def inference_pipeline(input_text, model, text_preprocessor, tokenizer, device):
    model.eval()

    cleaned_text=text_preprocessor.clean_text(input_text)
    input_encodings = tokenizer([cleaned_text], truncation=True, padding="max_length", max_length=512, return_tensors="pt")

    inputs = {
        'input_ids': input_encodings['input_ids'].to(device),
        'attention_mask': input_encodings['attention_mask'].to(device)
    }

    with torch.no_grad():
        outputs = model(**inputs)

    # Pulls the highest probability class
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

    max_probs, argmax_classes = torch.max(probs, dim=1)

    # If probability is lower or equal to 0.65, it keeps the class, otherwise returns class 4 (Unsure).
    final_predictions = torch.where(max_probs >= 0.65, argmax_classes, 4)

    # 7. Maps final probabilities back to classes
    class_labels_mapping = {
        0: "Pure Human Written",
        1: "Pure AI Written",
        2: "Human Text Rewritten by AI (Polished)",
        3: "AI Text Rewritten by Human (Humanised)",
        4: "Unsure (Below 65% Confidence Boundary Threshold)"
    }

    predicted_id = final_predictions.item()
    confidence_percentage = max_probs.item()

    print("CUSTOM THRESHOLD SINGLE INFERENCE ANALYSIS REPORT\n")

    print(f"Evaluated Model Confidence : {confidence_percentage:.2%}")
    print(f"Final Categorized Prediction: Class {predicted_id} : {class_labels_mapping[predicted_id]}")

