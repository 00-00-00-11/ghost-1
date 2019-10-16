from flask import Flask, request
from celery import Celery
import os
import task

app = Flask(__name__)
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'


@app.route('/')
def index():
    result = task.hello.delay('cool msg')
    result.wait()
    print(result.result)
    return f'Hello, world! {result}'


@app.route('/testing', methods=['POST'])
def test():
    json_data = request.get_json()
    print(json_data)
    return json_data


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
