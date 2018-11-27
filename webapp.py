
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')
@app.route("/page1")
def render_page1():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('page1.html')
  def getDataOptions(counties):
    myList=[] 
    for county in counties:
        if not county["State"] in myList:
            myList.append (county["State"])
    options = ""
    for state in myList:
        options=options + Markup("<option value=\"" + state + "\">" + state + "</option>")
    return options
if __name__=="__main__":
    app.run(debug=False, port=54321)
