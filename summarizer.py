from transformers import pipeline

# create a summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# your input text
text = """
Transformers are powerful deep learning models that use self-attention mechanisms.
They can process entire sequences of text at once, which makes them much faster
and better than older models like RNNs or LSTMs. Transformers are used in chatbots,
translation, summarization, and more.
"""

# summarize
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

print("\n=== Original Text ===\n", text)
print("\n=== Summary ===\n", summary[0]['summary_text'])
