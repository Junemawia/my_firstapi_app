
from fastapi import FastAPI
import random

# 1. Initialize the API
app = FastAPI(title="June's Capstone API")

# A list of jokes to be used in the dynamic endpoint
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Real programmers count from 0.",
    "A SQL query walks into a bar, walks up to two tables, and asks, 'Can I join you?'"
]
# 2. Create a "Home" endpoint
@app.get("/")
def home():
    return {
        "Status": "Online",
        "Bot_Name": "June-Bot 1.0",
        "Message": "Welcome to my Capstone API Toolkit!"
    }
# 3. Create a "Dynamic" endpoint that returns a random joke
@app.get("/joke")
def get_joke():
    # Returns a random joke from our list
    return {"joke": random.choice(JOKES)}

@app.get("/motivate/{name}")
def motivate_user(name: str):
    return {
        "greeting": f"Hello {name}!",
        "motivation": "You're a grown-up—you've got this code under control!"
    }