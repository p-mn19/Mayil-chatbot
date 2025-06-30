from indic_transliteration.sanscript import transliterate, ITRANS, MALAYALAM

def correct_mixed_input(text):
    try:
        # Transliterate Manglish (written in ITRANS style) to Malayalam
        malayalam_text = transliterate(text, ITRANS, MALAYALAM)

        return {
            "ml": malayalam_text,
            "manglish": text,
            "en": f"Corrected spelling (Malayalam): {malayalam_text}"
        }

    except Exception as e:
        return {
            "ml": "ക്ഷമിക്കണം, തിരുത്താൻ കഴിഞ്ഞില്ല.",
            "manglish": text,
            "en": "Sorry, couldn't correct that."
        }
