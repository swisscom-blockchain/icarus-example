from flask import Flask, jsonify, abort
import logging


log = logging.getLogger('server')
app = Flask(__name__)


@app.route('/', methods=['GET'])
def health():
    return "Hello Switzerland"


def main():
    app.run(host='0.0.0.0', port='8080', debug=True, extra_files=['.'])


if __name__ == '__main__':
    main()
