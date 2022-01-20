from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
from google.oauth2 import id_token as google_id_token
from google.auth.transport import requests as google_requests


class Auth_Token(BaseModel):
    id_token: str
    access_token: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key="secret-string")

GOOGLE_CLIENT_ID = "990351908927-skb7qrco82tqb5a9em7aid0gukd1s82s.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"

@app.get("/places")
async def all_places():
    return {
        "places":{
            "warangalfort":{
                "placename":"warangalfort",
                "placelat":"28.0235",
                "placelong":"52.214",
                "distfromstay":"20"
            },
            "bhadrakalitemple":{
                "placename":"bhadrakalitemple",
                "placelat":"25.075",
                "placelong":"42.48",
                "distfromstay":"10"
            },
            "wonderla":{
                "placename":"wonderla",
                "placelat":"74.07",
                "placelong":"14.87",
                "distfromstay":"50"
            },
            "s2cinemas":{
                "placename":"s2cinemas",
                "placelat":"51.87",
                "placelong":"84.87",
                "distfromstay":"5"
            }
        }
    }

@app.post("/googlesignin")
async def google_signin(auth_token:Auth_Token):
    idtoken = auth_token.id_token
    # accesstoken = auth_token.access_token
    request = google_requests.Request()
    id_info = google_id_token.verify_oauth2_token(idtoken, request, GOOGLE_CLIENT_ID)
    user_id = id_info['sub']
    user_email = id_info['email']
    print(user_id," : ",user_email)
    return {
        "userd_id":user_id,
        "user_email":user_email
    }

