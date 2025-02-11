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

cred = credentials.Certificate(os.path.join(os.getcwd(), "serviceAccountKey.json"))
firebase_admin.initialize_app(cred)

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
