import spacy

nlp = spacy.load('en_core_web_sm')

def morphologicalAnalysis(text):
    doc = nlp(text)

    for token in doc:
        # Print the token and the results of morphological analysis
        print("The orginal word is: ", token)
        print("The stem word is: ", token.lemma_)
        print(token.morph)

morphologicalAnalysis("cats")
morphologicalAnalysis("played")
