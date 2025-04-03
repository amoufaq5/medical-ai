# chat_interface/chat.py

from flask import Flask, request, jsonify
import os
import datetime

app = Flask(__name__)
LOG_DIR = "chat_logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def save_conversation(user_id, message):
    # Create a unique log file per user; in production, add encryption and secure storage.
    filename = os.path.join(LOG_DIR, f"{user_id}.txt")
    timestamp = datetime.datetime.now().isoformat()
    with open(filename, "a") as f:
        f.write(f"{timestamp}: {message}\n")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id")
    user_message = data.get("message")
    
    # Save the user input
    save_conversation(user_id, f"User: {user_message}")
    
    # Here you would integrate your diagnostic logic, e.g., call the model inference,
    # run through the diagnostic frameworks, and generate a response.
    # For demo, we return a dummy response.
    response = f"Received your message: {user_message}. How long have you experienced these symptoms?"
    
    # Save the system response
    save_conversation(user_id, f"System: {response}")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
