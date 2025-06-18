"""Scenario 4: Text Pre-processing
Task: Clean a text column in a DataFrame by:

1. Converting to lowercase.

2. Removing special characters (e.g., !, @).

3. Tokenizing the text."""

import pandas as pd
import re

# Updated sample data
df = pd.DataFrame({
    'text': [
        "Learning Python @ home!!",
        "Data Cleaning is important.",
        "AI & ML are the future!",
        "100% effort = success :)"
    ]
})

# Basic cleaning function
def clean_text(text):
    text = text.lower()  # 1. Lowercase
    text = re.sub(r'[^a-z0-9\s]', '', text)  # 2. Remove special characters
    tokens = text.split()  # 3. Tokenize
    return tokens

# Apply the function
df['tokens'] = df['text'].apply(clean_text)

# Output
print(df)
