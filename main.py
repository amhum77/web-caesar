from flask import Flask, request
app = Flask(__name__)
app.config['DEBUG']=True

form= """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{{
                background-color: #eee;
                padding: 20px;
                margin:0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
        textarea{{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>
    <form method="post">
    <label for ="rot">Rotate by:</label>
    <input id = "rot" type= "text" name="rot" value="0">
    <textarea name= "text">{0}</textarea>
    <input type="submit">
    </form> 
    </body>
</html>
"""
from caesar import rotate_string
@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rotate= request.form['rot']
    rotate=int(rotate)
    text = request.form['text']
    rotated_string = rotate_string(text, rotate)
    return form.format(rotated_string)

app.run()


