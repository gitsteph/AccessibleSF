from flask import Flask, request, render_template, redirect, flash, jsonify, url_for, send_from_directory
from flask import session
from flask_debugtoolbar import DebugToolbarExtension
import routes
import os


app = Flask(__name__)

app.secret_key = "###"

@app.route("/", methods=["GET"])
def main():
    accessible_MUNI_stops_list = routes.list_accessible_MUNI_stops()
    return render_template("index.html", good_MUNI=accessible_MUNI_stops_list)

##############################################################################

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))

    app.run(debug=False, host="0.0.0.0", port=PORT)
    # To use the DebugToolbar, uncomment below:
    # DebugToolbarExtension(app)
