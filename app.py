from flask import Flask, request, jsonify
from automate import summarize_article

app = Flask(__name__)

@app.route("/is_running", methods=['GET'])
def is_running():
    return "Server is running"

@app.route("/summarise_article", methods=['POST'])
def summarize():
    if request.method == 'POST':
        data = request.get_json()
        text = data['text']
        summary = summarize_article(text)
        return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(debug=True)

