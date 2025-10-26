# Create README
echo "# Transformer Text Summarizer

A simple project using a pretrained transformer (facebook/bart-large-cnn)
to summarize long text.

## Run
pip install torch transformers
python3 summarizer.py
" > README.md

# Create .gitignore
echo "__pycache__/
*.pyc
.cache/
.env/" > .gitignore

# Create requirements.txt
pip freeze > requirements.txt
