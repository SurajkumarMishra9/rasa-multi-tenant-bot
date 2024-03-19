from flask import Flask, request, jsonify
import requests  # Import for making external requests

app = Flask(__name__)

@app.route('/<variable_name>', methods=['POST'])
def handle_request(variable_name):
    # Extract variable from the URL path
    extracted_value = variable_name
    request_data = request.get_json()
    if variable_name=="suraj":
        target_url = f"http://localhost:5006/webhooks/rest/webhook"

        try:
            response = requests.post(target_url, json=request_data)
            response.raise_for_status()  # Raise an exception for non-2xx response codes
        except requests.exceptions.RequestException as e:
            return jsonify({'error': f"Error forwarding request: {str(e)}"}), 500

        # Check for successful response
        if response.status_code == 200:
            return jsonify(response.json())  # Return the response data as JSON
        else:
            return jsonify({'error': 'Error fetching data from target API'}), response.status_code

    elif variable_name=="binary":
                


        target_url = f"http://localhost:5005/webhooks/rest/webhook"

        try:
            response = requests.post(target_url, json=request_data)
            response.raise_for_status()  # Raise an exception for non-2xx response codes
        except requests.exceptions.RequestException as e:
            return jsonify({'error': f"Error forwarding request: {str(e)}"}), 500

        # Check for successful response
        if response.status_code == 200:
            return jsonify(response.json())  # Return the response data as JSON
        else:
            return jsonify({'error': 'Error fetching data from target API'}), response.status_code

    else:
        return jsonify({'error': f"Incorrect BOT ID"}), 500
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production use
