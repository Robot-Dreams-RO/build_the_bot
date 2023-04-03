import spacy

nlp = spacy.load("en_core_web_sm")

def get_response(user_input):
    doc = nlp(user_input)

    # Check for date entities
    dates = [ent for ent in doc.ents if ent.label_ == "DATE"]

    if dates:
        response = f"[INFO]: I found the following dates in your message: {', '.join([date.text for date in dates])}."
    else:
        response = "[ERROR]: I couldn't find any dates in your message."

    return response


print("[INFO]: Type something to begin, or type 'quit' to exit...")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break

    response = get_response(user_input)
    print("SpaCy_chatbot:", response)
