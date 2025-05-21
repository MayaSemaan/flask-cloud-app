from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello from Flask on Render!</h1><p>This is a live cloud app.</p>'

if __name__ == '__main__':
    app.run()