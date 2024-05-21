from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloworld():
    return "Hello World!"        

@app.route("/mae")
def suamae():
    return "Sua mãe é uma chachorra"    


if __name__ == '__main__':
    app.run(debug=True)