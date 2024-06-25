from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    # URL of the external API
    external_api_url = 'https://ifconfig.co/json'
    
    try:
        # Make a request to the external API
        response = requests.get(external_api_url)
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Get the JSON data from the response
        data = response.json()
        
        # Return the JSON data as a response
        return jsonify(data), 200
    
    except requests.exceptions.RequestException as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
