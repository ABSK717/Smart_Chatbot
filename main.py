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

# Find the closest match with at least 90% similarity
def find_best_match(query, responses, threshold=0.90):
    best_match = None
    best_score = 0
    for stored_query in responses:
        score = SequenceMatcher(None, query, stored_query).ratio()
        if score > best_score and score >= threshold:
            best_match = stored_query
            best_score = score
    return best_match

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
                responses[user_input].append(user_response)
            else:
                responses[user_input] = [user_response]
            
            save_responses(responses)
            print("Chatbot: Got it! I'll remember that for next time.")

# Run the chatbot
chatbot()
