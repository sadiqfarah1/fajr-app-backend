from fastapi import FastAPI, HTTPException
import firebase_admin
from firebase_admin import credentials, auth
from dotenv import load_dotenv
import os




# Load environment variables
load_dotenv()

app = FastAPI()

# Initialize Firebase

import os
import json
import firebase_admin
from firebase_admin import credentials

firebase_credentials_json = os.getenv("FIREBASE_CREDENTIALS")

if firebase_credentials_json:
    firebase_credentials = json.loads(firebase_credentials_json)
    cred = credentials.Certificate(firebase_credentials)
    firebase_admin.initialize_app(cred)
else:
    raise ValueError("Firebase credentials not found in environment variables")


@app.get("/")
def home():
    return {"message": "Fajr App Backend Running"}

# User registration/login (Firebase Auth)
@app.post("/login/")
def login_user(token: str):
    try:
        decoded_token = auth.verify_id_token(token)
        user_id = decoded_token["uid"]
        return {"status": "success", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# Track Fajr prayer
@app.post("/track_fajr/")
def track_fajr(user_id: str):
    return {"status": "success", "message": f"Fajr prayer logged for {user_id}"}

# Run server with: uvicorn main:app --reload
