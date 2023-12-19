from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True , port = 8999)
