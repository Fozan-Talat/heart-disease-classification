import flask
import pickle
import numpy as np

# Load the pickled model
with open('model_xgb.bin', 'rb') as f:
    model = pickle.load(f)

# Create a Flask app
app = flask.Flask(__name__)

# Define the API endpoint for classification
@app.route('/classify', methods=['POST'])
def classify():
    # Get the application data from the request body
    application_data = flask.request.get_json()

    # Convert the application data to a numpy array
    vector = np.array([application_data])

    # Make a prediction using the model
    prediction = model.predict(vector)[0]

    # Determine the classification status based on the prediction
    if prediction > 0.7:
        classification_status = "High risk"
    elif prediction > 0.5:
        classification_status = "Risk"
    else:
        classification_status = "Healthy"

    # Return the classification status as JSON
    return flask.jsonify({
        "status": classification_status
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=7860)