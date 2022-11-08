from distutils.command.config import config
from flask import Flask,jsonify,render_template,request
from models.utils import HeartTest
import config

app =Flask(__name__)

@app.route("/")
def hello():

    return render_template("index.html")

@app.route("/heart_disease",methods=["POST","GET"])
def Disease_prediction():

    if request.method == "POST":

        age=int(request.form.get("age"))
        sex=int(request.form.get("sex"))
        cp= int(request.form.get("cp"))
        trestbps=int(request.form.get("trestbps"))
        fbs=int(request.form.get("fbs"))
        restecg=int(request.form.get("restecg"))
        thalach=int(request.form.get("thalach"))
        exang=int(request.form.get("exang"))
        oldpeak=int(request.form.get("oldpeak"))
        slope=int(request.form.get("slope"))
        chol=int(request.form.get("chol"))
        ca=int(request.form.get("ca"))
        thal=int(request.form.get("thal"))


        heart_pred=HeartTest(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        heart_disease=heart_pred.Heart_test()
        print(heart_disease)

        return render_template("index.html",prediction=heart_disease)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER,debug=True)
