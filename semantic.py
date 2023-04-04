import spacy

nlp = spacy.load('en_core_web_md')

# Interesting note about the results.
# Monkey and Cat have a high similarity because they are both
# animals. Banana and Monkey also have a high similarity because
# monkeys eat and are associated with bananas. Cat and banana have
# the lowest similarity because a cat would not be associated with a banana.
# Another example of this might be te words: house, apartment and garden

print("-----Semantic Similarity-----")
word1 = nlp("cat")  # house
word2 = nlp("monkey")  # apartment
word3 = nlp("banana")  # garden
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print()

tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print()

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# In the example.py file when running the code with the simpler language
# model 'en_core_web_sm' the similarity between the sentences changes.
