from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    try:
        # Make a GET request to the specified URL
        response = requests.get('https://www.hughbrien.com')
        response.raise_for_status()  # Raise an error for bad status codes

        # Return the response content
        return jsonify({
            'status': 'success',
            'data': response.text
        })
    except requests.RequestException as e:
        # Handle any errors that occur during the request
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)
