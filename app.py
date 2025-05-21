from flask import Flask
app = Flask(_name_)

@app.route('/')
def home():
    return '<h1>Hello from Flask on Render!</h1><p>This is a live cloud app.</p>'

if _name_ == '_main_':
    app.run()