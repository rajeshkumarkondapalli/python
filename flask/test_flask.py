from flask import Flask, request
app = Flask(__name__)


@app.route('/ping/', methods=["GET", "POST"])
def hello():
    return "Hello World!"

@app.route('/test1', methods=['GET'])
def test1():
    a = request.args.get("a")
    return str(a)

@app.route('/test2', methods=['POST'])
def test2():
    a = request.form["a"]
    return str(a)

@app.route('/predict/house', methods=['POST'])
def predict():
    size = request.form["size"]
    return str(size)


if __name__ == '__main__':
    app.run(port=7000)