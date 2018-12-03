
from flask import Flask, url_for, render_template, request
import os
import json
app = Flask(__name__)
with open('drugs json.json') as demographics_data:
        agegroup = json.load(drugs_data)
        
@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
    if
    
    
     agegroup = request.args['agegroup']
    response= "ALCHOHOL USE:In 2016 9.2 percent or 2.3 million kids age 12-17, 57.1 percent or 19.8 million adults age 18-25 currently used alchohol, and 54.6 percent or 114.7 million adults age 26 and older. An estimation of how many people age 12 or older were binge alchohol drinkers in the past 30 days in 2016 was 65.3 million people which is about 24.2 percent. BINGE DRINK WITHIN THE PAST MONTH: Aproximately 4.9 percent of kids 2-17, 38.4 percent of adults age 18-25, and 24.2 percent of adults of 26 and older are current binge drinkers. In 2016 it was reported that there where aproximately 65.3 million people age 12 or older that werebinge drinkers in the past month. HEAVY ALCHOHOL USE: 6 percent of people age 12 and older are heavy alchohol users. 0.8 percent of kids age 12-17, 10.1 percent of adaults age 18-25, and 6 percent of adaults age 26 and up are heavy alchohol users. AVERAGE ALCHOHOL USE: In 2016 it was reported that 7.3 million people fromt he age 12-20 had reported drinking alchohot within the pas month, the legal age to dink in the U.S is 21. About 3/5 (62.5%) of underaged drinkers were binge drinkers, and about 1/7 (14.7%) were heavy alchohol users."
   
    
    
    
    return render_template('page1.html')

def fact()
   
if __name__=="__main__":
    app.run(debug=False, port=54321)

  
