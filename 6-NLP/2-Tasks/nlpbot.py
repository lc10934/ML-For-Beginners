import random
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor
print("Hello, I am Marvin, the simple robot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today?")
extractor = ConllExtractor()

while True:
    user = input("> ")
    user_input_blob = TextBlob(user, np_extractor=extractor)  # note non-default extractor specified
    np = user_input_blob.noun_phrases  
    if user== "bye":
        break
    if user_input_blob.polarity <= -0.5:
        response = "Oh dear, that sounds bad. "
    elif user_input_blob.polarity <= 0:
        response = "Hmm, that's not great. "
    elif user_input_blob.polarity <= 0.5:
        response = "Well, that sounds positive. "
    elif user_input_blob.polarity <= 1:
        response = "Wow, that sounds great. "
    if len(np) != 0:
        response = response + "Can you tell me more about " + np[0].pluralize() + "?"
    else:
        response = response + "Can you tell me more?"
    print(response)
print("It was nice talking to you, goodbye!")