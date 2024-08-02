from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/result/<name>/<int:age>')
def result(name, age):
    if (age>=18):
        y=age-18
        return f'{name}, You are eligible to vote.'f' You are eligible to vote since last {y} years.'
    else:
        x=18-age
        return f'{name}, You are not eligible to vote yet.' f'.......... you can vote after {x}  years'
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        return redirect(url_for('result', name=name, age=age))
    else:
        name = request.args.get('name')
        age = int(request.args.get('age'))
        return redirect(url_for('result', name=name, age=age))
if __name__ == '__main__':
    app.run()