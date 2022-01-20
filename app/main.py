from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from authlib.integrations.starlette_client import OAuth
from authlib.integrations.starlette_client import OAuthError


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
GOOGLE_CLIENT_ID = "990351908927-skb7qrco82tqb5a9em7aid0gukd1s82s.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"

config_data = {'GOOGLE_CLIENT_ID': GOOGLE_CLIENT_ID, 'GOOGLE_CLIENT_SECRET': GOOGLE_CLIENT_SECRET}
starlette_config = Config(environ=config_data)
oauth = OAuth(starlette_config)
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

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
async def google_signin(request:Request):
    try:
        access_token = await oauth.google.authorize_access_token(request)
    except OAuthError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    return({
        "access-token" : access_token
    })