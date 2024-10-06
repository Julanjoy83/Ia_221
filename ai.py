import openai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Set your API key
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('user_query')

    # Using GPT-4 with the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "This is a chatbot that can converse on a wide range of topics."},
            {"role": "user", "content": user_query}
        ]
    )
    chatbot_response = response.choices[0].message['content']

    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
