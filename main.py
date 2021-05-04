from flask import Flask, render_template, request, redirect
from shortener import Shortener

app = Flask("lazycnt")

shortener = Shortener()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/short", methods=["POST"])
def short():
    redirect_url = request.form["redirect_url"]
    shortened_url = "http://lazy.cnt/{}".format(shortener.generate_key(redirect_url))
    return render_template("short.html", shortened_url=shortened_url)

@app.route("/<key>")
def redirect_to(key):
    url = shortener.get_url(key)
    if url:
        return redirect(url)
    return "Key not found"

app.run("","80")
shortener.cleanup()