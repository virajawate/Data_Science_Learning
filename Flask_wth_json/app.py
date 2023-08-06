from flask import Flask, request, render_template, jsonify, redirect, url_for
import json
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("Welcome.html")


@app.route('/calculator', methods=['GET', 'POST'])
def operations():
    if request.method == 'GET':
        try:
            with open('flask/templates/Calculator.json', 'r') as json_form:
                form_data = json.load(json_form)
                print("form rendered")
            return render_template("Calculator.html", form_data=form_data)
        except FileNotFoundError:
            return "Error : File Not Found", 404
    elif request.method == 'POST':
        # if request.headers['Content-Type'] != "application/json":
        #     return jsonify({"Error" : "Content Type must be 'application/json'"}), 400
        try:
            print("temp here")
            jsons = request.form
            operate = jsons["operation"]
            number_1 = float(jsons["number_1"])
            number_2 = float(jsons["number_2"])
            if operate == "add":
                result = number_1 + number_2
                print(result)
            elif operate == "sub":
                result = number_1 - number_2
            elif operate == "mul":
                result = number_1 * number_2
            elif operate == "div":
                if number_2 != 0:
                    result = number_1 / number_2
                else:
                    print("INVALID INPUT")
                    result = "INF"
            else:
                return jsonify({"Error" : "Invalid Operation...."}), 400
            
            result_data = {"result" : result}
            print("Calculated Result:", result)  
            with open('flask/templates/Result.json', 'w') as result_file:
                json.dump(result_data, result_file)
                print("Saved Result Data:", result_data)
            return redirect(url_for('final'))
        except Exception as e:
            return str(e), 400

@app.route('/result')
def final():
    try:
        with open('flask/templates/Result.json', 'r') as result_file:
            result_data = json.load(result_file)
            print("Retrieved Result Data:", result_data)  # Debugging
            result = result_data["result"]
            print("Retrieved Result:", result)  # Debugging
    except Exception as e:
        return "Error: Result File Not Found", 404
    
    return render_template('Result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)