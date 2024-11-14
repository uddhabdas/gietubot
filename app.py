from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response  # Import the function that generates chatbot responses
import os

app = Flask(__name__)
CORS(app)  # Enable CORS to handle cross-origin requests

# Route for rendering the main page
@app.route("/", methods=["GET"])
def index_get():
    return render_template("bas.html")

# Route for handling chat requests
@app.route("/predict", methods=["POST"])
def predict():
    # Get the user's message from the JSON payload
    text = request.get_json().get("message")
    
    # Validate that a message was provided
    if not text:
        return jsonify({"error": "No message provided"}), 400

    # Get the chatbot's response
    response = get_response(text)
    
    # Return the response as JSON
    return jsonify({"answer": response})

# Main entry point
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the port from the environment variable
    app.run(debug=True, host="0.0.0.0", port=port)
