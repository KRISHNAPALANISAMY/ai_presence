import sqlite3

from transformers import pipeline

# Initialize transformers for more advanced text generation
nlp = pipeline('text-generation', model='gpt2')


# Function to connect to the knowledge database
def connect_db():
    return sqlite3.connect('ai_knowledge.db')


# Function to check if the AI already knows the answer
def get_answer_from_db(question):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM knowledge WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return None


# Function to store new knowledge
def store_knowledge(question, answer):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO knowledge (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()


# Function to interact with the user
def interact_with_ai():
    print("Hello! I am your AI friend. How can I help you today?")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        # Check if the AI knows the answer to the question
        answer = get_answer_from_db(user_input)

        if answer:
            print(f"AI: {answer}")
        else:
            print("AI: I don't know the answer to that. Could you teach me?")
            new_answer = input("You: ").strip()
            store_knowledge(user_input, new_answer)
            print(f"AI: Thanks! I will remember that.")


# Start the interaction
interact_with_ai()
