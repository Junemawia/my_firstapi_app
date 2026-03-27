FastAPI Beginner’s Toolkit

1. Project Overview
This project is a lightweight, high-performance API built using FastAPI. It was designed as a beginner-friendly entry point into modern backend development, focusing on speed, automatic documentation, and ease of use.

2. Why FastAPI?
I chose FastAPI for this toolkit because:

Instant Documentation: It automatically generates an interactive UI (Swagger) so anyone can test the API without writing a single line of client-side code.

Speed: It is one of the fastest Python frameworks available, making it perfect for scalable applications.

Ease of Learning: The use of Python type hints makes the code more readable and reduces bugs.

3. How to Run This Project
Follow these steps to get the API running on your local machine:

Extract the project folder and open it in VS Code.

a.Create a Virtual Environment:

PowerShell
python -m venv venv

b.Activate the Environment:

Windows: .\venv\Scripts\activate

c.Install Dependencies:

PowerShell
pip install -r requirements.txt
Start the Server:

PowerShell
uvicorn main:app --reload
Test the API: Open your browser and go to http://127.0.0.1:8000/docs.

4. AI Prompt Journal (Use of GenAI)
To build this toolkit, I collaborated with an AI assistant. Key prompts and problem-solving steps included:

Environment Setup: "How do I activate a virtual environment in PowerShell when I get an Execution Policy error?"

Prompt: "I am an Applied Computer Science student. Explain the core architecture of FastAPI compared to traditional frameworks like Flask. Use a 'Restaurant' analogy to explain how an API Request and Response works."

Prompt: "Explain the core architecture of FastAPI "

AI Response: Summarize: The API is the waiter, the Client is the diner, and the Server is the kitchen.

Prompt: "Give me a step-by-step guide to setting up a FastAPI project in VS Code."

AI Response: pip install fastapi uvicorn

Prompt: "Give me a step-by-step terminal guide to setting up a virtual environment in VS Code for a FastAPI project. Include the commands to install fastapi and uvicorn, and explain why I need both."

Error Handling: "Why does the && token fail in my terminal?" (Resolved by running commands individually for better compatibility).

Code Implementation: "How do I create a dynamic greet endpoint in FastAPI?"

5. Common Issues & Fixes

Error: "I am getting a '422 Unprocessable Entity' error when I try to send data to my FastAPI endpoint. Explain what this error means in plain English and show me how to fix my Pydantic model to resolve it."

Error: Execution_Policies restriction.

Fix: I used the command Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process to allow the activation script to run securely.

Error: failed to locate pyvenv.cfg.

Fix: This occurred when the environment was modified while active. I resolved it by deleting the venv folder and rebuilding it from scratch.

6. Peer Testing & Feedback
The API was tested by navigating to the /docs endpoint.
Tester: [Harun]
Date: March 27, 2026

Test Case 1: Dynamic Greeting (GET)
Instruction: I asked the tester to go to /greet/ and add their name to the URL.

Result: The API successfully returned: {"message": "Hello [Name], FastAPI is working!"}.

Feedback: "It's cool that the URL changes the message instantly."

7. References
https://fastapi.tiangolo.com/  
https://realpython.com/get-started-with-fastapi/

# difference between flask and fast api
While both flask and fast api are Python-based, the fundamental difference lies in their philosophy: Flask is a "micro-framework" that prioritizes simplicity and flexibility, requiring developers to manually handle data validation and documentation, whereas FastAPI is a modern, high-performance framework built for speed and efficiency. FastAPI leverages Python's type hints to provide automatic data validation and interactive Swagger documentation out-of-the-box, features that usually require extra libraries in Flask. Furthermore, FastAPI is natively asynchronous, making it significantly faster at handling multiple simultaneous requests compared to Flask’s traditionally synchronous architecture.





