from flask import Flask, render_template, request
from do import func
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['u']
        password = request.form['p']
        func(username, password)
        return render_template('done.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
