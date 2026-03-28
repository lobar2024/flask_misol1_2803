from flask import Flask, render_template

app = Flask(__name__)

# 1
@app.route('/')
def home():
    name = 'Ali'
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
