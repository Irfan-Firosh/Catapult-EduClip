from sentence_transformers import SentenceTransformer, util
from GeminiSimilarSentences import *
from segment import *

model = SentenceTransformer("all-MiniLM-L6-v2")



# Function that returns a dictionary
#a, kumbucket2 = getSegment("M42uDLGRSpI", 50)



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
    originals = similar_request(original)
    #originals = [original]

    embed1 = model.encode(originals, convert_to_tensor= True)
    embed2 = model.encode(values, convert_to_tensor=True)

    cosine_scores = util.cos_sim(embed1, embed2)
    max_values = []
    for row in cosine_scores:
        max_values.append(max(row))

    return max_values
    

# Main code
def kum(id, Question):

    to_return, kumbucket2 = getSegment(id, 50) 
    original_string = Question
    cosine_scores = similarity(original_string, kumbucket2)

    pairs = []
    for i in range(len(cosine_scores)):
        pairs.append({"index": i, "score": cosine_scores[i]})
    
    # Sort pairs based on similarity scores
    pairs = sorted(pairs, key=lambda x: x["score"], reverse=True)

    # Get the indexes of top 5 similar sentences
    top_indexes = [pair["index"] for pair in pairs[:5]]

    # Extract corresponding elements from to_return using top_indexes
    corresponding_elements = [to_return[index] for index in top_indexes]

    return corresponding_elements
