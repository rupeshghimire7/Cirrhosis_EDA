# Liver_Cirrhosis_Prediction
The Liver Cirrhosis Prediction is a project done as Final_requirement for FusemachinesAI Fellowship: Machine Learning 

This aims to detect the stage of cirrhosis using various biomarkers of patients.

The file contains: EDA part and Prediction Part


## liver_cirrhosis_prediction

This Flask application aims to predict the presence of liver cirrhosis in patients using a set of biomarkers. The prediction model is built upon various clinical factors and laboratory results, including the following biomarkers:

N_Days: Number of days since the initial diagnosis or assessment.
Age: The age of the patient.
Ascites: Presence or absence of ascites (abnormal accumulation of fluid in the abdomen).
Hepatomegaly: Presence or absence of hepatomegaly (enlargement of the liver).
Spiders: Presence or absence of spider angiomas (spider-like blood vessels on the skin).
Bilirubin: Bilirubin levels in the blood.
Cholesterol: Cholesterol levels in the blood.
Albumin: Albumin levels in the blood.
Copper: Copper levels in the blood.
Triglycerides: Triglyceride levels in the blood.
Platelets: Platelet count.
Prothrombin: Prothrombin time (a measure of blood clotting time).
To make a prediction, the application takes these biomarker values as input and provides an output indicating the likelihood of liver cirrhosis. The prediction model has been trained on a dataset containing a diverse range of patient samples, and it utilizes machine learning algorithms to make accurate predictions.


## Usage

Clone the repository:

```
git clone git@github.com:rupeshghimire7/Liver_Cirrhosis_Prediction.git
```
Go to liver-cirrhosis-prediction file
```
cd liver-cirrhosis-prediction
```

Install the required dependencies using pip:


```
pip install -r requirements.txt
```

Run the Flask application:
```
cd service
```
```
python app.py
```
OR:
```
python3 app.py
```

Access the application through your web browser at http://127.0.0.1:5000/predict

Enter the values for the biomarkers mentioned above into the provided input fields.

Click the "Predict" button to obtain the liver cirrhosis prediction result.

![image](https://github.com/rupeshghimire7/Liver_Cirrhosis_Prediction/assets/62866358/fd07bb6b-b70a-4712-b91c-3b5595a80143)
