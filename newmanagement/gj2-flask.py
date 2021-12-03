from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
   return 'This is the second program done by Jhansi and Kavitha'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug = True)
