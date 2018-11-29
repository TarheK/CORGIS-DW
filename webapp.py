
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
    response= 
    <ul>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ul> 
    return render_template('response.html', response = response)
   
if __name__=="__main__":
    app.run(debug=False, port=54321)

  
