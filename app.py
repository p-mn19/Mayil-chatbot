from flask import Flask, request, jsonify
from flask_cors import CORS
from intent_classifier import classify_intent
from translator import translate
from corrector import correct_mixed_input
import random

app = Flask(__name__)
CORS(app)

greetings = [
    {"en": "Hello!", "ml": "ഹലോ!", "manglish": "halo!"},
    {"en": "Hi!", "ml": "ഹായ്!", "manglish": "hai!"},
    {"en": "Namaskaram!", "ml": "നമസ്കാരം!", "manglish": "namaskaram!"}
]

farewells = [
    {"en": "Goodbye!", "ml": "വിട", "manglish": "vida"},
    {"en": "See you!", "ml": "വീണ്ടും കാണാം", "manglish": "veendum kaanam"}
]

chat_replies = [
    {"en": "How are you?", "ml": "സുഖമാണോ?", "manglish": "sukhamaano?"},
    {"en": "I'm fine.", "ml": "ഞാൻ സുഖമാണ്", "manglish": "njan sukhamaanu"},
    {"en": "Nice to meet you!", "ml": "കണ്ടതിൽ സന്തോഷം!", "manglish": "kandathil santhosham!"}
]

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').strip()

    if not user_input:
        return jsonify({'en': "Please say something!", 'ml': "ദയവായി എന്തെങ്കിലും പറയൂ!", 'manglish': "dayavaayi enthengilum parayu!"})

    intent = classify_intent(user_input)

    if intent == 'greet':
        return jsonify(random.choice(greetings))
    elif intent == 'translate':
        return jsonify(translate(user_input))
    elif intent == 'correct':
        corrected = correct_mixed_input(user_input)
        return jsonify({
            'en': f"Corrected: {corrected}",
            'ml': f"ശുദ്ധമാക്കിയത്: {corrected}",
            'manglish': f"shuddhamakkiyathu: {corrected}"
        })
    elif intent == 'bye':
        return jsonify(random.choice(farewells))
    else:
        return jsonify(random.choice(chat_replies))

if __name__ == '__main__':
    app.run(debug=True)