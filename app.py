from flask import Flask, request, jsonify, render_template
from ChatSQL import ChatWithSql

app = Flask(__name__)
obj = ChatWithSql("postgres", "", "localhost", "Olympics")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    query = request.form.get('query')
    if not query:
        return jsonify({"error": "Query not provided"}), 400

    response = obj.message(query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
