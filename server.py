{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
import requests\
\
app = Flask(__name__)\
\
# Configurazione Supabase\
SUPABASE_URL = "https://wydwootdyrunenoorgnj.supabase.co/rest/v1/"\
SUPABASE_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind5ZHdvb3RkeXJ1bmVub29yZ25qIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE0NDI4NzgsImV4cCI6MjA1NzAxODg3OH0.Z4x3YUReisxfLIq1uctDVEmTNLEqhwd6hgM0uGEg9KU"\
\
# Endpoint API di prova\
@app.route('/get_sigilli', methods=['GET'])\
def get_sigilli():\
    headers = \{\
        "apikey": SUPABASE_API_KEY,\
        "Authorization": f"Bearer \{SUPABASE_API_KEY\}",\
        "Content-Type": "application/json"\
    \}\
    \
    response = requests.get(f"\{SUPABASE_URL\}Sigilli", headers=headers)\
    \
    if response.status_code == 200:\
        return jsonify(response.json())\
    else:\
        return jsonify(\{"error": response.text\}), response.status_code\
\
if __name__ == '__main__':\
    app.run(host='0.0.0.0', port=5000)\
}