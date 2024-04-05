from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a dictionary to store the votes
votes = {'option1': 0, 'option2': 0}

@app.route('/')
def index():
    return render_template('index.html', votes=votes)

@app.route('/vote', methods=['POST'])
def vote():
    option = request.form['option']
    if option in votes:
        votes[option] += 1
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
