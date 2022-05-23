from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world(name = None):

    return render_template('index.html')


@app.route('/chart')
def chartShow():
    return render_template('TestHTML.html')

if __name__ == '__main__':
    app.run(debug=True)
