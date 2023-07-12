
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
            <h1> Flask Project </h1>
            <div id='
            '''
app.debug = True

app.run()