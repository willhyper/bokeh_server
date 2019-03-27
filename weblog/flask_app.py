from bokeh.embed import server_document
from flask import render_template, Flask, request

from weblog import data_renderer, data_holder

addr = '0.0.0.0'
port = 8000

app = Flask(__name__)


@app.route('/', methods=['GET'])
def bkapp_page():
    script = server_document(data_renderer.url)
    return render_template("embed.html", script=script)


@app.route('/', methods=['POST'])
def post_data():
    rj = request.get_json()
    data_holder.post(**rj)

    return "ack"
