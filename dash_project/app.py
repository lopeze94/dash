from flask import Flask, render_template
from bokeh.embed import autoload_server
from bokeh.client import pull_session
app = Flask(__name__)


@app.route("/")
def index():
    session = pull_session(url="http://localhost:5006/flask_radius")
    bokeh_script = autoload_server(None, url="http://localhost:5006/flask_radius", session_id=session.id)
    return render_template("index.html", bokeh_script=bokeh_script)


if __name__ == "__main__":
    app.run(debug=False)
