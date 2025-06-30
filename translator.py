translations = {
    "thank you": {
        "ml": "നന്ദി",
        "manglish": "nandi",
        "en": "Thank you"
    },
    "how are you": {
        "ml": "സുഖമാണോ?",
        "manglish": "sughamano?",
        "en": "How are you?"
    },
    "my name is vaishnavi": {
        "ml": "എൻറെ പേര് വൈഷ്ണവി ആണ്",
        "manglish": "ente peru vaishnavi aanu",
        "en": "My name is Vaishnavi"
    }
}

def translate(text):
    text = text.lower().strip()
    normalized = ''.join(c for c in text if c.isalnum() or c.isspace())

    for key in translations:
        if key in normalized:
            return translations[key]

    return {
        "ml": "ക്ഷമിക്കണം, ഞാൻ വിവർത്തനം ചെയ്യാനായില്ല.",
        "manglish": "kshamikkuka, njan vivarthanam cheyyan kazhiyilla.",
        "en": "Sorry, I don't know the translation."
    }
