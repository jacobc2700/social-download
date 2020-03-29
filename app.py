from flask import Flask, render_template, request

import os, json

# Make app.
app = Flask(__name__)

# Home route.
@app.route("/home")
def home():
    return render_template("home.html")

# Download from Instagram.
@app.route("/instagram", methods=["GET", "POST"])
def instagram():
    if request.method == 'POST':
        account_name = request.form['account_name']
        os.system("instaloader " + account_name)
        return render_template("instagram.html")
    else:
        return render_template("instagram.html")

# Download from VSCO.
@app.route("/vsco", methods=['GET', 'POST'])
def vsco():
    if request.method == 'POST':
        account_name = request.form['account_name']
        os.system("vsco-scraper " + account_name + " --getImages")
        return render_template("vsco.html")
    else:
        return render_template("vsco.html")

# Download from Twitter.
@app.route("/twitter", methods=['GET', 'POST'])
def twitter():
    if request.method == 'POST':
        account_name = request.form['account_name']
        os.system('twitterscraper ' + account_name + ' -u -o temporary.json')
        os.system('python -m json.tool < temporary.json > ' + account_name + '.json')
        os.remove('temporary.json')
        return render_template('twitter.html')
    return render_template("twitter.html")

# Run application in debug mode.
if __name__ == '__main__':
    app.run(debug=True)