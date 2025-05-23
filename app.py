from flask import Flask, render_template
from signal_logic import generate_signal

app = Flask(__name__)

@app.route('/')
def home():
    signal = generate_signal()
    return render_template('index.html', signal=signal)

if __name__ == '__main__':
    app.run(debug=True)
