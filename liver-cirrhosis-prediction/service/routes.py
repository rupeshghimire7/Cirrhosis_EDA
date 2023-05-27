from flask import  Blueprint,render_template, request
import numpy as np
import joblib

bp = Blueprint('predict_routes', __name__)


# Load the saved model
scaler = joblib.load('../models/scaler.joblib')
ada_best = joblib.load('../models/ada_best.joblib')
ada_full = joblib.load('../models/ada_full.joblib')
bag_best = joblib.load('../models/bag_fs.joblib')
rf = joblib.load('../models/rf_full.joblib')
svm = joblib.load('../models/svm.joblib')

best_cols = np.array([ 0,  2,  4,  5,  6,  8,  9, 10, 11, 13, 15, 16])

@bp.route('/predict')
def index():
    return render_template('form.html')

# Define a route to handle incoming requests
@bp.route('/predict', methods=['POST'])
def predict():
    features = process(request.form).reshape(1,-1)
    features = scaler.transform(features)
    model = request.form['Model']
    if model=='ada-best':
        prediction = ada_best.predict(features[:,best_cols])
    elif model=='ada_full':
        prediction = ada_full.predict(features)
    elif model=='bag_best':
        prediction = bag_best.predict(features[:,best_cols])
    elif model=='rf':
        prediction = rf.predict(features)
    else:
        prediction = svm.predict(features[:,best_cols])
    print("Model: ",model," ,prediction: ",prediction[0])

    message = "Tha patient might have stage 4 cirrhosis.It's critical!" if prediction[0]==4 else "The patient might have stage 3 cirrhosis. Immediate treatment required!" if prediction[0]==3 else "The patient might have stage 2 cirrhosis. Recommend him/her a healthy routine!"
    return {"prediction":int(prediction[0]),"message":message}

def process(form):
    n_days = int(request.form['N_Days'])
    drug = int(request.form['Drug'])
    age = float(request.form['Age'])
    sex = int(request.form['Sex'])
    ascites = int(request.form['Ascites'])
    hepatomegaly = int(request.form['Hepatomegaly'])
    spiders = int(request.form['Spiders'])
    edema = int(request.form['Edema'])
    bilirubin = float(request.form['Bilirubin'])
    cholesterol = float(request.form['Cholesterol'])
    albumin = float(request.form['Albumin'])
    copper = float(request.form['Copper'])
    alk_phos = float(request.form['Alk_phos'])
    sgot = float(request.form['SGOT'])
    tryglicerides = float(request.form['Tryglicerides'])
    platelets = float(request.form['Platelets'])
    prothrombin = float(request.form['Prothrombin'])

    features = np.array([n_days,drug,age,sex,ascites,hepatomegaly,spiders,edema,bilirubin,cholesterol,albumin,copper,alk_phos,sgot,tryglicerides,platelets,prothrombin])

    # features[8:] = np.log(features[8:])
    

    return features
