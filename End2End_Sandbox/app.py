from src.DiamondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict_datapoints():
    if request.method == "GET":
        return render_template("Form.html")
    else:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut= request.form.get('cut'),
            color = request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        
        final_data = data.get_data_as_df()
        
        predict_pipeline = PredictPipeline()
        
        pred = predict_pipeline.predict(final_data)
        
        result = round(pred[0], 2)
        
        return render_template("Result.html", final_result = result)

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "GET":
        return render_template("Result.html")


app.run(debug=True)

"""sumary_line
src.DiamondPricePrediction.exception.CustomException: Error occured in the file name [C:\Users\viraj\Documents\GitHub\Data_Science_Learning\End2End_Sandbox\src\DiamondPricePrediction\pipelines\prediction_pipeline.py] line number [19] error message [Cannot use median strategy with non-numeric data:
could not convert string to float: 'SI2']
Keyword arguments:
argument -- description
Return: return_description
"""
