from flask import Flask, render_template, request, jsonify, session
from search_agent import search_agent
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key in production

@app.route('/')
def index():
    if 'search_history' not in session:
        session['search_history'] = []
    return render_template('index.html', search_history=session['search_history'])

@app.route('/search', methods=['POST'])
def search():
    question = request.form['question']
    answer = search_agent(question)
    
    # Add search to history
    search_entry = {
        'question': question,
        'answer': answer,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    session['search_history'].append(search_entry)
    session.modified = True
    
    return jsonify({'answer': answer})

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['search_history'] = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, port=8000)