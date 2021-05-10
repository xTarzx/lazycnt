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
        generated_key = shortener.generate_key(redirect_url)
        if generated_key["error"]:
            return render_template("index.html", error=generated_key["error"])
        return render_template("index.html", domain=domain, key=generated_key["key"])
    return render_template("index.html")

@app.route("/<key>")
def redirect_to(key):
    url = shortener.get_url(key)
    if url:
        return redirect(url)
    return render_template("index.html", error="Tf is that key")

app.run("","80")
shortener.cleanup()