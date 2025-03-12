from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)