
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    return render_template('page1.html')
@app.route("/response1")
def render_response1():
    agegroup = request.args['agegroup']
    response= "In 2016 9.2 percent or 2.3 million kids age 12-17 currently used alchohol, 57.1 percent or 19.8 million adults age 18-25 currently used alchohol, and 54.6 percent or 114.7 million adults age 26 and older currently used alchohol"
    return render_template('response.html', response = response)
   
if __name__=="__main__":
    app.run(debug=False, port=54321)

  
