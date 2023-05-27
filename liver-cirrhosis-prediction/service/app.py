# ['N_Days', 'Age', 'Ascites', 'Hepatomegaly', 'Spiders',
# 'Bilirubin','Cholesterol', 'Albumin', 'Copper', 'Tryglicerides',
#  'Platelets','Prothrombin']

# ['N_Days', 'Drug', 'Age', 'Sex', 'Ascites', 'Hepatomegaly', 'Spiders',
#        'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos',
#        'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']

       
from flask import Flask, redirect, url_for
import routes
from routes import bp


app=Flask(__name__,template_folder='.')

app.config['SECRET_KEY'] = "blablabla"
app.register_blueprint(bp)


@app.route("/")
def home():
	return redirect(url_for('predict_routes.index'))

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
