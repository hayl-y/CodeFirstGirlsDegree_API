import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Fern Facts</h1>" \
           "<p>This site is a prototype API for plant lovers, to find out more about their plants.</p>"

app.run()