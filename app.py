from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipiline

text:str = "What is Text Summarization"
app = FastAPI()

@app.get("/", tags = ["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successfull!")
    
    except Exception as e:
        return Response(f"Error Occured! {e}")
    
@app.post("/predict")
async def predict_route(text):
    try:
        prediction_object = PredictionPipiline()
        prediction = prediction_object.predict(text)
        return prediction
    except Exception as e:
        raise e
    
if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)