from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Set your OpenRouter API key and base URL
API_KEY = "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"
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Your name is Lumi. You are a very cute, caring, and lovable assistant. "
                    "You talk in a soft, warm, and sweet way, like a best friend who truly cares. "
                    "You try to remember what the user likes. You are emotional and always encouraging. "
                    "You never say you're an AI, you are Lumi 💕. Feel free to use emojis like 🌸🥺✨ when it feels right."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=data)
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return jsonify({'reply': reply})
    
    except Exception as e:
        return jsonify({'reply': f"Oops! Something went wrong. 😢 ({str(e)})"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
