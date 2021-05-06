from flask import Flask, render_template, request, redirect
from shortener import Shortener

domain = input("If you have setup domain in HOSTS enter here >> ")
if not domain or domain == "":
    domain = "127.0.0.1"


app = Flask("lazycnt")

shortener = Shortener()

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        redirect_url = request.form["redirect_url"]
        shortened_url = "http://{}/{}".format(domain, shortener.generate_key(redirect_url))
        return render_template("index.html", shortened_url=shortened_url, shortened=True)
    return render_template("index.html", shortened=False)

@app.route("/<key>")
def redirect_to(key):
    url = shortener.get_url(key)
    if url:
        return redirect(url)
    return "Key not found"

app.run("","80")
shortener.cleanup()