from fastapi import FastAPI

# 1. Initialize the API
app = FastAPI(title="June's Capstone API", description="A beginner-friendly toolkit for FastAPI")

# 2. Create a "Home" endpoint
@app.get("/")
def home():
    return {
        "Status": "Online",
        "Message": "Welcome to my FastAPI Toolkit!",
        "Next_Step": "Go to /docs to test the API visually"
    }

# 3. Create a "Dynamic" endpoint
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello {name}, FastAPI is working perfectly!"}