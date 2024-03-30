from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")



# Function that returns a dictionary
random_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A stitch in time saves nine.",
    "Actions speak louder than words.",
    "All good things must come to an end.",
    "Beauty is in the eye of the beholder.",
    "Better late than never.",
    "Birds of a feather flock together.",
    "Don't count your chickens before they hatch.",
    "Every cloud has a silver lining.",
    "Fortune favors the bold."
]

# Generate the dictionary
def generate_dictionary():
    dictionary = {}
    for i, sentence in enumerate(random_sentences):
        dictionary[i] = sentence
    return dictionary



# Function that calculates similarity
def similarity(original, values):
    # Dummy implementation
    result = {}
    originals = [original]

    embed1 = model.encode(originals, convert_to_tensor= True)
    embed2 = model.encode(values, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embed1, embed2)
    return cosine_scores
    

# Main code
if __name__ == "__main__":
    # Call the function to generate the dictionary
    my_dict = generate_dictionary()

    # Extract the values (2nd column) from the dictionary

    # Call the similarity function
    original_string = "Similar people are within themselves"
    cosine_scores = similarity(original_string, random_sentences)

    # Print the similarity scores
    pairs = []
    for i in range(cosine_scores.shape[0]):
        for j in range(cosine_scores.shape[1]):
            pairs.append({"index": [i, j], "score": cosine_scores[i][j]})

        # Sort scores in decreasing order
    #pairs = sorted(pairs, key=lambda x: x["score"], reverse=True)

    for i in range(10):
        print("{} \t\t Index: {} \t\t Score: {:.4f}".format(
        random_sentences[i], pairs[i]["index"], pairs[i]["score"]
    ))