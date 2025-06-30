import re

def classify_intent(text):
    text = text.lower().strip()

    greeting_keywords = ['hello', 'hi', 'namaskaram', 'namaste', 'hey', 'hai', 'ഹായ്', 'നമസ്കാരം']
    bye_keywords = ['bye', 'exit', 'quit', 'goodbye', 'വിട', 'പോകുന്നു']
    translate_keywords = ['thank', 'nandi', 'what is', 'meaning', 'translate', 'അര്‍ത്ഥം', 'വ്യാഖ്യാനം']
    correct_keywords = ['correct', 'right spelling', 'wrong', 'mistake', 'ശുദ്ധമാക്കുക', 'കുറവ്']

    if any(word in text for word in greeting_keywords):
        return 'greet'
    elif any(word in text for word in translate_keywords):
        return 'translate'
    elif any(word in text for word in correct_keywords):
        return 'correct'
    elif any(word in text for word in bye_keywords):
        return 'bye'
    else:
        return 'chat'
