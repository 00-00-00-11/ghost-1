from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/testing', methods=['POST'])
def test():
    json_data = request.get_json()
    print(json_data)


if __name__ == '__main__':
    app.run(debug=True)
