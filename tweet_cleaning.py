import re

def cleaning(texte):
    # Remove URLs
    texte = re.sub(r"http\S+|www\S+|https\S+", "", texte, flags=re.MULTILINE)
    
    # Remove leading and trailing spaces from text.
    texte = texte.strip()
    
    # Remove emojy
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', texte)
    

#Exemple d'utilisation
#texte = "          Voici un exemple de texte avec une URL https://example.com et un émoji 😊."
#texte_nettoye = cleaning(texte)
#print(texte_nettoye)
