from flask import Flask
import app as home


app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
