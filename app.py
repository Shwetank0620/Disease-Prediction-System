from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    os.system("python main.py")
    return render_template('index.html')

@app.route('/heart')
def heart():
    return render_template('heart.html')

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')

@app.route('/lung-cancer')
def lung_cancer():
    return render_template('lung-cancer.html')

@app.route('/breast-cancer')
def breast_cancer():
    return render_template('breast-cancer.html')

@app.route('/result')
def result():
    outcome = ""
    return render_template('result.html', result = outcome)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)