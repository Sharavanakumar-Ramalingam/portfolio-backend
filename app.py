from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# ✅ Use Groq API key from environment variable
groq_client = Groq(api_key="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")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        messages = data.get("messages", [])
        if not messages:
            return jsonify({"error": "No messages provided"}), 400

        completion = groq_client.chat.completions.create(
            model="llama3-70b-8192",  # or your preferred model
            messages=messages,
            temperature=1,
            max_tokens=1024,
            top_p=1
        )

        # ✅ Return as a serializable JSON response
        return jsonify(completion.model_dump())

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port
    app.run(host="0.0.0.0", port=port)
