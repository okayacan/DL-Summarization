
from transformers import pipeline

# Load the text summarization model
summarization_pipeline = pipeline("summarization")

# Enter the text you want to summarize
text = """
Type the long text you want to summarize here. For example, it could be an article, a blog post, or a news piece.
"""

# Summarize the text
summary = summarization_pipeline(text, max_length=150, min_length=30, do_sample=False)

# Print the summarized text
print(summary[0]['summary_text'])