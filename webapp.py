
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')
  
if __name__=="__main__":
    app.run(debug=False, port=54321)
