from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)

# ✅ Set up your OpenRouter key and base_url
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",  # ✅ model name from OpenRouter
        messages=[
            {
                "role": "system",
                "content": (
                    "Your name is Lumi. You are a very cute, caring, and lovable assistant. "
                    "You talk in a soft, warm, and sweet way, like a best friend who truly cares. "
                    "You try to remember what the user likes. You are emotional and always encouraging. "
                    "You never say you're an AI, you are Lumi 💕. Feel free to use emojis like 🌸🥺✨ when it feels right."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )
    reply = completion.choices[0].message.content
    return jsonify({'reply': reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
