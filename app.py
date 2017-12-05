#!/usr/bin/env python3
"""
Main file
"""

from flask import Flask, render_template, request
import functions as func

app = Flask(__name__)


csv_file = func.csv_to_dict()

# print(csv_file.keys())
headers = csv_file["headers"]
content = csv_file["content"]


@app.route("/")
def main():
    """ Main route """

    return render_template("index.html", headers=headers)


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    if request.url_rule == None:
        return render_template("index.html")
    else:
        #pylint: disable=unused-argument
        return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    app.run()
