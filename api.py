from typing import Dict
from fastapi import Depends, FastAPI
from pydantic import BaseModel
import json

from model import Model, get_model

app = FastAPI()

model = Model()

@app.post("/inference")
def inference(sentence : str):
    result = model.inference(sentence)
    return {'result':result}

if __name__ == '__main__':
    uvicorn.run(app, host='local_host', port=8000)