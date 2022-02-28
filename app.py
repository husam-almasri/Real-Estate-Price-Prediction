# import os

from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_area_names')
def get_area_names():
    util.load_saved_artifacts()
    response = jsonify({
        'Area_type': util.get_area_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_location_names')
def get_location_names():
    util.load_saved_artifacts()
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    util.load_saved_artifacts()
    bedrooms = int(request.form['bedrooms'])
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    area_type = request.form['area_type']
    location = request.form['location']

    response = jsonify({
        'estimated_price': util.get_estimated_price(bedrooms, total_sqft, bath, balcony, area_type, location)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(debug=True)
