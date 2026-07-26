# Smart_Chatbot
> A lightweight Rule-Based Self-Learning Chatbot built with Python that learns new responses during conversations and stores them locally in a JSON database.

Unlike traditional hardcoded chatbots, this chatbot can remember new question-response pairs provided by the user. It uses fuzzy string matching to recognize similar questions and retrieve the most appropriate response.

## Features

- Learn new responses during conversations
- Store learned knowledge permanently in JSON
- Fuzzy matching using Python's `difflib.SequenceMatcher`
- Multiple responses for the same question
- Random response selection for natural conversations
- Display all learned knowledge
- Simple command-line interface
- No external libraries required

---

## How It Works

1. User asks a question.
2. The chatbot searches its knowledge base.
3. If a similar question (90% similarity or higher) exists:
   - A stored response is returned.
4. If no match is found:
   - The chatbot asks the user for the correct response.
   - The new question-response pair is saved into `responses.json`.
5. Future conversations can reuse the learned response.

---

## Project Structure

```
project/
│
├── main.py          # Main chatbot application
├── responses.json      # Knowledge base
└── README.md
```

---

## Technologies Used

- Python 3
- JSON
- difflib.SequenceMatcher
- Random module

---

## Commands

| Command | Description |
|----------|-------------|
| `!exit` | Exit the chatbot |
| `!bye` | Exit the chatbot |
| `!show responses` | Display all learned responses |
| `show what you learned` | Display the knowledge base |

---

## Example

```
You: Hello
Chatbot: I don't know the answer. Can you tell me?

how to respond to 'Hello'
Type Answer here:
Hi! Nice to meet you.

Chatbot: Got it! I'll remember that for next time.
```

Later...

```
You: Hello
Chatbot: Hi! Nice to meet you.
```

---

## Learning Process

```
User Input
     │
     ▼
Search JSON Knowledge Base
     │
     ├──────── Match Found ───────► Return Response
     │
     ▼
 No Match
     │
Ask User for Response
     │
Store in JSON
     │
Future Conversations Use It
```

---

## Current Limitations

- Uses character similarity instead of semantic understanding.
- Cannot understand context.
- No intent classification.
- No natural language processing (NLP).
- Case-sensitive similarity may affect matching.
- Responses depend entirely on previously learned data.

---

## Future Improvements
- GUI
- SQLite database


---

## Author

Abhishek Kumar
