from flask import Flask, request, jsonify
import difflib
from transformers import GPT2LMHeadModel, GPT2Tokenizer
app = Flask(__name__)

# Пример документов для проверки на плагиат
documents = [
    "This is a test document.",
    "This document is very similar to a test document.",
    "This is a completely different document."
]

# Проверка на плагиат
@app.route('/check_plagiarism', methods=['POST'])
def check_plagiarism():
    input_text = request.json['text']
    max_similarity = 0
    for doc in documents:
        similarity = difflib.SequenceMatcher(None, input_text, doc).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
    plagiarism_percentage = max_similarity * 100
    return jsonify({'plagiarism': plagiarism_percentage})

# Проверка на ИИ
