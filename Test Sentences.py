from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")



# Function that returns a dictionary
kumbucket = [
    {
        "text": "[Music]",
        "start": 1.12,
        "duration": 15.56
    },
    {
        "text": "let's find 24 to the power 38 modulo 7",
        "start": 12.019,
        "duration": 6.52
    },
    {
        "text": "and I'm going to use a little from all",
        "start": 16.68,
        "duration": 5.22
    },
    {
        "text": "little theorem in here so 24 to the 38",
        "start": 18.539,
        "duration": 5.701
    },
    {
        "text": "modulo 7 first thing I'll note is that",
        "start": 21.9,
        "duration": 6.449
    },
    {
        "text": "24 actually is is larger than seven so",
        "start": 24.24,
        "duration": 6.39
    },
    {
        "text": "I'm going to first say that 24 to this",
        "start": 28.349,
        "duration": 5.191
    },
    {
        "text": "38 is actually congruent to well let's",
        "start": 30.63,
        "duration": 4.859
    },
    {
        "text": "see what's the remainder when 24 is",
        "start": 33.54,
        "duration": 5.76
    },
    {
        "text": "divided by 7 7 goes in 3 times 4 21 with",
        "start": 35.489,
        "duration": 6.211
    },
    {
        "text": "a remainder of 3 so this is the same as",
        "start": 39.3,
        "duration": 6.0
    },
    {
        "text": "3 to the 38 modulo 7 remember we're",
        "start": 41.7,
        "duration": 7.23
    },
    {
        "text": "working modulo 7 okay since 3 & 7 are",
        "start": 45.3,
        "duration": 5.7
    },
    {
        "text": "relatively prime and P is a prime that",
        "start": 48.93,
        "duration": 7.14
    },
    {
        "text": "means that 3 to the power of P minus 1",
        "start": 51.0,
        "duration": 8.1
    },
    {
        "text": "which be 6 here is congruent let's put",
        "start": 56.07,
        "duration": 6.329
    },
    {
        "text": "this in a different color actually 3 to",
        "start": 59.1,
        "duration": 5.61
    },
    {
        "text": "the power of P minus 1 which is 6 is",
        "start": 62.399,
        "duration": 6.691
    },
    {
        "text": "congruent to 1 mod 7 and that would be",
        "start": 64.71,
        "duration": 6.96
    },
    {
        "text": "by for Maw's little theorem 3 to the",
        "start": 69.09,
        "duration": 6.029
    },
    {
        "text": "power 6 is congruent to 1 mod 7 so that",
        "start": 71.67,
        "duration": 4.47
    },
    {
        "text": "means I'm going to take this one right",
        "start": 75.119,
        "duration": 3.781
    },
    {
        "text": "here and take that power of 38 on the 3",
        "start": 76.14,
        "duration": 7.44
    },
    {
        "text": "and change this into 3 ^ let's see",
        "start": 78.9,
        "duration": 7.8
    },
    {
        "text": "what's 38 2 divided by 6 would be 6",
        "start": 83.58,
        "duration": 7.289
    },
    {
        "text": "copies of 6 for 36 plus 2 so that would",
        "start": 86.7,
        "duration": 8.9
    },
    {
        "text": "be congruent to 3 to the 6th to the 6th",
        "start": 90.869,
        "duration": 9.531
    },
    {
        "text": "times by 3 squared ok now remember 3 to",
        "start": 95.6,
        "duration": 6.57
    },
    {
        "text": "the 6 by 4 loss little theorem is",
        "start": 100.4,
        "duration": 4.29
    },
    {
        "text": "congruent to 1 so this is the same as 1",
        "start": 102.17,
        "duration": 6.72
    },
    {
        "text": "to the 6th times 3 squared and of course",
        "start": 104.69,
        "duration": 6.719
    },
    {
        "text": "1 does the sixth is 1 and 3 squared is",
        "start": 108.89,
        "duration": 5.64
    },
    {
        "text": "just 9 so this is congruent to 9 but",
        "start": 111.409,
        "duration": 6.031
    },
    {
        "text": "remember the whole problem was modulo 7",
        "start": 114.53,
        "duration": 5.01
    },
    {
        "text": "so what is the remainder when you divide",
        "start": 117.44,
        "duration": 3.539
    },
    {
        "text": "9 by 7",
        "start": 119.54,
        "duration": 5.82
    },
    {
        "text": "well 7 goes into 9 one time with 2 left",
        "start": 120.979,
        "duration": 4.981
    },
    {
        "text": "over",
        "start": 125.36,
        "duration": 3.06
    },
    {
        "text": "so overall the final answer to this",
        "start": 125.96,
        "duration": 4.74
    },
    {
        "text": "problem is that the remainder modulo 7",
        "start": 128.42,
        "duration": 4.86
    },
    {
        "text": "is going to be the answer is 2 so the",
        "start": 130.7,
        "duration": 5.99
    },
    {
        "text": "final answer to the problem is 2",
        "start": 133.28,
        "duration": 3.41
    }
]

# Generate the dictionary
#def generate_dictionary():
 #   dictionary = {}
  #  for i, sentence in enumerate(random_sentences):
   #     dictionary[i] = sentence
    #return dictionary



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
    #my_dict = generate_dictionary()

    # Extract the values (2nd column) from the dictionary

    # Call the similarity function
    original_string = "What is remainder theorem"
    random_sentences = [entry["text"] for entry in kumbucket]
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