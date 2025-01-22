import sqlite3

# Create or connect to the database
conn = sqlite3.connect('ai_knowledge.db')
cursor = conn.cursor()

# Create a table to store the knowledge
cursor.execute('''
CREATE TABLE IF NOT EXISTS knowledge (
    id INTEGER PRIMARY KEY,
    question TEXT,
    answer TEXT
)
''')

# Commit changes and close
conn.commit()
conn.close()
