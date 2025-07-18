from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"  # Replace with your real key
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
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
    app.run(debug=True)
