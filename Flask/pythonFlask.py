import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Witaj, świecie"

app.run(port='8000')
