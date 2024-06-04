from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        
        return render_template('result.html', message="Hello")

if __name__ == '__main__':
    app.run(debug=True)
