from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load dataset into a dictionary
dataset = {
    "Hello": "Namaskaram, How can i help you?",
    "How are you?": "Njan sukhamaayirikkunnu.(I'm fine!) Ningal enganeyaanu? (How are you?)",
    "I'm also fine": "ath nallathan!(that's good) in malayalam you reply with- enicum sukham tonnunnu. ",
    "enicum sukham tonnunnu": "kollam! nee nannayi cheyyunnu.(yes excellent! you are doing great!)",
    "What is your name?": "Ente peru Mayil aanu. (My name is Mayil) endan ningaludeth? (What is yours?)",
    "My name is Nima": "Hello Nima! in malayalam you reply with- Ente peru Nima aanu",
    "Ente peru Nima aanu": "athishayakaram!(Amazing)  Ninte kandu santhoshamaayi.(Nice to meet you!)",
    "How do I say thank you in Malayalam?": "Athu 'Nandi' aanu. (It is 'Nandi')",
    "Where are you going?": "In malayam you ask: Ningal evide poykondirikkunnu?",
    "Ningal evide poykondirikkunnu?": "Njan market-il poykondirikkunnu. (I am going to the market)",
    "What is your favorite color?": "In malayalam we ask: Ninte ishtamulla niram enthanu?",
    "Ninte ishtamulla niram enthanu?": "shari! Ente ishtamulla niram nilaa aanu. (My favorite color is blue.)",
    "Do you like reading books?":"In malayalam we ask: Ningalk pusthakam vayikkan ishtamaano?",
    "Ningalkk pusthakam vayikkan ishtamaano?": "Athe, enikye pusthakam vayikkunnath ishtamaanu. (Yes, I love reading.)",
    "Njann varunnu illa": "Njann varunnu is correct, not Njann varunnu illa. (The phrase I am coming is correct; the negated form is incorrect.)",
    "nee enda chiyunadu?":"Always use 'Ningal' for respectful 'you'. (Use the respectful version of 'you' in formal conversations.)",
    "ningal enda chiyunadu?":"Correct!"
}

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    reply = dataset.get(user_message, "Sorry, I don't understand that.")
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
