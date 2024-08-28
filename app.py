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
@app.route('/check_ai', methods=['POST'])
def check_ai():
    input_text = request.json['text']
    # Это просто пример, реальная проверка на ИИ может быть более сложной
    ai_score = len(input_text) % 100  # Для демонстрации, здесь будет всегда разный результат
    return jsonify({'ai_score': ai_score})

# Генерация текста с использованием GPT-2
@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.json['prompt']
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)
