from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__, template_folder='.')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy-sms', methods=['POST'])
def proxy_sms():
    data = request.json
    phone = data.get('phone')
    message = data.get('message')
    gateway_ip = data.get('gateway_ip')

    if not all([phone, message, gateway_ip]):
        return jsonify({"error": "Missing parameters"}), 400

    # Ensure URL is correct
    gateway_ip = gateway_ip.strip().rstrip('/')
    url = f"{gateway_ip}/send-sms"

    try:
        print(f"Sending SMS to {phone} via {url}")
        response = requests.post(url, json={
            "phone": phone,
            "message": message
        }, timeout=10)
        
        return jsonify({
            "status": "success",
            "gateway_response": response.json() if response.status_code == 200 else response.text
        })
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Talli Server starting at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
