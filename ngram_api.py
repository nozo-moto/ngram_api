from flask import Flask, request

app = Flask(__name__)


def ngram(text: str, num: int) -> list:
    return "".join([("".join([text[(len(text) + j + i ) % len(text)] for j in range(num)]) + "\n") for i in range(len(text))])


@app.route('/post', methods=['POST'])
def ngrame_post():
    request_data = request.json
    text = request_data['text']
    num = request_data['num']
    return "".join([i for i in ngram(text, int(num))])

if __name__ == '__main__':
    app.run()
