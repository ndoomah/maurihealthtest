import nltk
from nltk import sent_tokenize
from fuzzywuzzy import process
nltk.download('punkt')

# DISEASE TERMS FOR FUZZY STRING MATCHING
diseaseterms = ['influenza', 'gastroenteritis', 'conjunctivitis', 'respiratory infection',
                'infectious disease',
                'diarrhea', 'pink eye', 'got gastro', 'got flu', 'disease virus', 'coughing', 'cough',
                'caught cold',
                'high fever', 'fever', 'headache', 'aches and pains', 'sore throat', 'dizziness',
                'vomiting',
                'stomach pain', 'cramps', 'nausea', 'dehydration', 'eye redness', 'itching of eye',
                'eye swelling',
                'eye tearing', 'sneezing', 'nasal congestion', 'runny nose', 'nasal breathing', 'diarrhée',
                'conjonctivite', 'grippe', 'gastro-entérite', 'infection respiratoire',
                'maladie infectieuse',
                'gastro', 'grippe', 'virus de la maladie', 'toux', 'pris froid',
                'forte fièvre', 'fièvre', 'maux de tête', 'douleurs', 'maux de gorge', 'vertiges',
                'vomissement',
                'douleurs estomac', 'crampes', 'nausées', 'déshydratation', 'rougeur des yeux',
                'démangeaisons oculaires',
                'gonflement des yeux',
                'larmoiement des yeux', 'éternuements', 'congestion nasale', 'nez qui coule', 'respiration nasale']

# LOCATION TERMS FOR FUZZY STRING MATCHING
places_terms = ['port louis', 'beau bassin', 'rose hill', 'curepipe', 'quatre bornes', 'vacoas', 'phoenix',
                    'plaines wilhems', 'moka', 'reduit', 'rivière noire', 'albion', 'amaury', '	rivière du rempart',
                    'flacq', 'anse la raie', 'arsenal', 'baie du cap', 'pamplemousses', 'baie du tombeau', 'bambous',
                    'savanne', 'grand port', 'beau vallon', 'bel air rivière sèche', 'bel ombre', 'benares',
                    'bois cheri',
                    'bois des amourettes', 'bon accueil', 'brisee verdiere', 'britannia', 'calebasses', 'camp carol',
                    'camp de masque', 'camp diable', 'camp ithier', 'camp thorel', 'cap malheureux', 'cascavelle',
                    'case noyale', 'chamarel', 'chamouny', 'chemin grenier', 'flic en flac', 'goodlands', 'grand baie',
                    'grand bel air', 'grand bois', 'grand gaube', 'grande riviere noire', 'la flora', 'lalmatie',
                    'mahebourg', 'mapou', 'midlands', 'pailles', 'plaine magnien', 'riviere des anguilles',
                    'rose belle',
                    'saint pierre', 'souillac', 'surinam', 'tamarin', 'terre rouge', 'triolet', 'tyack', 'verdun']


#---- FUNCTIONS extract_location AND extract_disease IMPLEMENTS TEXT ANALYSIS---#

def extract_location(content, score):
    sentences = sent_tokenize(content)
    # convert to lower case
    tokens = [w.lower() for w in sentences]

    location = ""

    for token in tokens:
        print(token)
        x = process.extractOne(token, places_terms, score_cutoff=score)

        if x is not None:
            location = location + str(x)

    return location

def extract_disease(content, score):
    sentences = sent_tokenize(content)
    # convert to lower case
    tokens = [w.lower() for w in sentences]
    disease = ""

    for token in tokens:
        print(token)
        x = process.extractOne(token, diseaseterms, score_cutoff=score)

        if x is not None:
            disease = disease + str(x)
    return disease
