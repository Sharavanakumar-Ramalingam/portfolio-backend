from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# ✅ Your Groq API Key
groq_client = Groq(api_key="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")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        messages = data.get("messages", [])

        completion = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=1,
            max_tokens=1024,
            top_p=1
        )

        # ✅ Convert to JSON-serializable dictionary
        return jsonify(completion.model_dump())

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
