from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import string
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings('ignore')

# Initial downloads (only once)
nltk.download('punkt')
nltk.download('wordnet')

# Initialize app
app = Flask(__name__)
CORS(app)

# Load dataset
with open('dialogs.txt', 'r', encoding='utf8') as f:
    raw_data = f.read().lower()

sent_tokens = raw_data.strip().splitlines()

lemmer = WordNetLemmatizer()

# Tokenizer and normalization functions
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greeting detection
GREETING_INPUTS = ("hello", "hi", "greetings", "hey", "namaskaram")
GREETING_RESPONSES = ["Hi!", "Hey there!", "Namaskaram!", "Hello!", "Greetings!"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Generate response using TF-IDF + cosine similarity
def generate_response(user_input):
    user_input = user_input.lower()
    sent_tokens.append(user_input)

    tfidf_vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = tfidf_vectorizer.fit_transform(sent_tokens)

    similarity_scores = cosine_similarity(tfidf[-1], tfidf)
    idx = similarity_scores.argsort()[0][-2]

    flat = similarity_scores.flatten()
    flat.sort()
    best_score = flat[-2]

    sent_tokens.pop()  # clean up

    if best_score == 0:
        return "Sorry, I didn't understand that."
    else:
        return sent_tokens[idx]

# Flask API route
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')

    if not user_message:
        return jsonify({'reply': "Please say something!"})

    if user_message.lower() in ['bye', 'exit', 'quit']:
        return jsonify({'reply': "Goodbye! Take care!"})

    greeting_response = greeting(user_message)
    if greeting_response:
        return jsonify({'reply': greeting_response})

    ai_reply = generate_response(user_message)
    return jsonify({'reply': ai_reply})

if __name__ == '__main__':
    app.run(debug=True)
