from flask import Flask, request 
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG']=True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method='post'>
        <label>Rotate by:
        <input type='text' name='rot' value='0'/>
        </label>
        <textarea type='text' name='text'>{0}</textarea>
        <input type='submit' value='Encrypt'/>
    </body>
</html>
"""
@app.route("/encrypt", methods=['POST'])
def encrypt_message():
    text = request.form['text']
    rot = int(request.form['rot'])
    e_message=encrypt(text, rot)
    return form.format(e_message)

@app.route("/")
def index():
    return form.format("")

app.run()