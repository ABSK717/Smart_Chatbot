import json
from difflib import SequenceMatcher

# Load existing queries and responses from JSON
def load_responses(file_path='responses.json'):
    try:
        with open(file_path, 'r') as file:
            responses = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # If file doesn't exist or is empty/invalid, start with an empty dictionary
        responses = {}
    return responses

# Save updated queries and responses to JSON
def save_responses(responses, file_path='responses.json'):
    with open(file_path, 'w') as file:
        json.dump(responses, file, indent=4)

# Get word overlap similarity Score
def word_similarity(a, b):
    a = set(a.lower().split())
    b = set(b.lower().split())
    return len(a & b) / len(a | b)

# Find the most similar stored query using a hybrid similarity approach.
def find_best_match(query, responses, threshold=0.90):

    scores = []
    # Score every stored query
    for stored_query in responses:
        # Character-level similarity
        fuzzy_match_score = SequenceMatcher(None, query, stored_query).ratio()
        # Word-level similarity
        word_match_score = word_similarity(query, stored_query)
        # Hybrid similarity score
        final_score = ( 0.5 * fuzzy_match_score + 0.5 * word_match_score )
        scores.append((stored_query, final_score))

    # No learned responses available
    if not scores:
        return None

    # Rank matches from highest to lowest confidence
    scores.sort(key=lambda x: x[1], reverse=True)
    best_match, best_score = scores[0] # pick top match with highest score

    # Return the best match only if it passes the confidence threshold
    if best_score >= threshold:
        print(f"Best match: '{best_match}' ({best_score:.2f})")
        return best_match

    # No match is confident enough
    return None
   

# Display all learned responses
def display_learned_responses(responses):
    if responses:
        print("Learned Responses:")
        for query, response in responses.items():
            print(f"- {query}: {', '.join(response)}")
    else:
        print("No learned responses yet.")

# Chatbot function
def chatbot():
    responses = load_responses()
    print("Chatbot is ready! Type '!exit' or '!bye' to end the conversation or 'show learned responses' to see learned responses.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == '!exit' or user_input.lower() == '!bye':
            print("Chatbot: Goodbye!")
            break
        elif user_input.lower() == 'show what you learned' or user_input.lower()=="!show responses":
            display_learned_responses(responses)
            continue
        
        # Find the best match in existing responses
        best_match = find_best_match(user_input, responses)
        
        if best_match:
            # Choose a random response if there are multiple
            import random
            response = random.choice(responses[best_match])
            print(f"Chatbot: {response}")
        else:
            print("Chatbot: I don't know the answer. Can you tell me?")
            user_response = input(f"how to respond to '{user_input}'\nType Answer here: ")
            
            # If the query already exists, append the new response
            if user_input in responses:
                responses[user_input].append(user_response.lower())
            else:
                responses[user_input] = [user_response]
            
            save_responses(responses)
            print("Chatbot: Got it! I'll remember that for next time.")

# Run the chatbot
chatbot()
