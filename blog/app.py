from time import time

from flask import Flask, request, g

app = Flask(__name__)


@app.route('/<string:search>', methods=['GET', 'POST'])
def index(search: str):
    """

    :param search:
    :return:
    """
    return f'hello, {request.method} !'


@app.before_request
def process_before_request():
    g.start_time = time()


@app.after_request
def process_after_request(response):
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time
    return response


@app.errorhandler(404)
def handler_484(error):
    app.logger.error(error)
    return '484'
