from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

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

