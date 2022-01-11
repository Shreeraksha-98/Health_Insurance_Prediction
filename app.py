from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("health_rf.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # age
        age = int(request.form["age"] )   
        
    
        # bmi
        bmi = float(request.form["bmi"] )   
        
        # children
        children = int(request.form["children"] )   
        
        # smoke
        smk = request.form["smoke"]   
        if (smk == 'Yes'):
            smoke = 1
        else:
            smoke = 0

        # gender
        gnd = request.form["gender"]   
        if (gnd == 'Male'):
            male = 1
            female = 0
        else:
            male = 0
            female = 1

       # region
        rgn = request.form["region"]   
        if (rgn == 'northeast'):
            northeast = 1
            northwest = 0
            southeast = 0
            southwest = 0
        elif (rgn == 'northwest'):
            northeast = 0
            northwest = 1
            southeast = 0
            southwest = 0
        elif (rgn == 'southeast'):
            northeast = 0
            northwest = 0
            southeast = 1
            southwest = 0
        else :
            northeast = 0
            northwest = 0
            southeast = 0
            southwest = 1
            

        

        
    #     ['age', 'bmi', 'children', 'smoke', 'male', 'female', 'northeast', 'northwest', 'southeast', 'southwest']
        
        prediction=model.predict([[
            age,
            bmi,
            children,
            smoke,
            male,
            female,
            northeast,
            northwest,
            southeast,
            southwest
        ]])


        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Insurance cost is $ {}".format(output))

          
    


if __name__ == "__main__":
    app.run(debug=True)
