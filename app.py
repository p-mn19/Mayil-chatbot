from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load dialogs.txt as Q&A pairs
qa_pairs = {}
with open('dialogs.txt', 'r', encoding='utf8') as f:
    lines = f.read().strip().splitlines()
    for i in range(0, len(lines)-1, 2):
        question = lines[i].strip().lower()
        answer = lines[i+1].strip()
        qa_pairs[question] = answer

# Matching logic
def find_answer(user_input):
    user_input = user_input.strip().lower()

    # Exact match
    if user_input in qa_pairs:
        return qa_pairs[user_input]

    # Partial match: look for keywords in questions
    for question in qa_pairs:
        if all(word in question for word in user_input.split()):
            return qa_pairs[question]

    # No match found
    return "Sorry, I don't know that yet. Try asking something else!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').strip()

    if not user_input:
        return jsonify({'reply': "Please say something!"})

    if user_input.lower() in ['bye', 'exit', 'quit']:
        return jsonify({'reply': "Goodbye! Take care!"})

    reply = find_answer(user_input)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
