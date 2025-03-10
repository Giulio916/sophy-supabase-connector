from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configurazione Supabase
SUPABASE_URL = "https://wydwootdyrunenoorgnj.supabase.co/rest/v1/"
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind5ZHdvb3RkeXJ1bmVub29yZ25qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE0NDI4NzgsImV4cCI6MjA1NzAxODg3OH0.Z4x3YUReisxfLIq1uctDVEmTNLEqhwd6hgM0uGEg9KU"

@app.route('/get_sigilli', methods=['GET'])
def get_sigilli():
    headers = {
        "apikey": SUPABASE_API_KEY,
        "Authorization": f"Bearer {SUPABASE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(f"{SUPABASE_URL}sigilli", headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
