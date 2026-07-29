import re
import pandas as pd


def has_repeating_sentences(text, min_sentence_length=25):
    """Returns True if any sentence of substantial length repeats inside the text."""
    text_str = str(text).strip()

    # Split text into sentences using standard punctuation boundaries (. ! ?)
    sentences = re.split(r"(?<=[.!?])\s+", text_str)

    # Clean sentences and filter out short fragments or empty strings
    clean_sentences = [
        s.strip() for s in sentences if len(s.strip()) >= min_sentence_length
    ]

    # Convert to a set to find unique items
    unique_sentences = set(clean_sentences)

    # If the counts match, every sentence is unique. If not, a loop occurred!
    return len(clean_sentences) != len(unique_sentences)


# 1. Load your raw master dataset
df_raw = df
initial_count = len(df_raw)

# 2. Apply the dynamic loop detector across the entire file
df_raw["is_looping"] = df_raw["generation"].apply(has_repeating_sentences)

# 3. Drop all looping rows along with the previous placeholder checks
df_clean = df_raw[
    (df_raw["generation"].str.len() > 150) &  # Increased from 50 to 150 to catch blog headers
    (~df_raw["generation"].str.contains(r"Posted in|Tagged |Leave a comment", case=False, na=False)) & # New web filter
    (~df_raw["generation"].str.lower().str.contains(r"\[full version")) & # Original check
    (~df_raw["generation"].str.contains(r"\.\.\.")) & # Original check
    (~df_raw["is_looping"])  # Original loop filter
].reset_index(drop=True)

# Remove the temporary boolean tracking column
df_clean = df_clean.drop(columns=["is_looping"])
df = df_clean
final_count = len(df_clean)
print(
    f"🧹 Data Cleansed! Removed {initial_count - final_count} total corrupted rows."
)
print(f"📊 Pristine source rows remaining: {final_count}")