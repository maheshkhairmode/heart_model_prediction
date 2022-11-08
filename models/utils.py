import numpy as np 
import pandas as pd 
import pickle
import json

class HeartTest():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
        self.age=age
        self.sex=sex
        self.cp=cp
        self.trestbps=trestbps
        self.chol=chol
        self.fbs=fbs
        self.restecg=restecg
        self.thalach=thalach
        self.exang=exang
        self.oldpeak=oldpeak
        self.slope=slope
        self.ca=ca
        self.thal=thal

    def Load_models(self):
        with open ("models\logistic_model_heart.pkl","rb")as f:
            self.model=pickle.load(f)

        with open ("models\heart_data.json","r")as f:
            self.data=json.load(f)


    def Heart_test(self):
        self.Load_models()
        array=np.zeros(len(self.data["columns"]))
        array[0]=self.age
        array[1]=self.sex
        array[2]=self.cp
        array[3]=self.trestbps
        array[4]=self.chol
        array[5]=self.fbs
        array[6]=self.restecg
        array[7]=self.thalach
        array[8]=self.exang
        array[9]=self.oldpeak
        array[10]=self.slope
        array[11]=self.ca
        array[12]=self.thal

        prediction_value=self.model.predict([array])[0]
        print("prediction value is",prediction_value)

        if prediction_value==1:
            return "PATIENT HAVING HEART PROBLEM"

        else:
            return "PATIENT IS ALRIGHT"

if __name__=="__main__":
    age=63.0
    sex=1.0
    cp=3.0
    trestbps=145.0
    fbs=1.0
    restecg=0.0
    thalach=150.0
    exang=0.0
    oldpeak=2.3
    slope=0.0
    chol=233.0
    ca=0.0
    thal=1.0

    heart_pred=HeartTest(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    heart_disease=heart_pred.Heart_test()
    print(heart_disease) 



