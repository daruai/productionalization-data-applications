# FastAPI model server for Iris dataset
# Path: model-servers/fast-api-server/app/app.py
# Run with: uvicorn app:app --reload

# 1. Create the data model
# 2. Load the model
# 3. Create the health check endpoint
# 4. Create the prediction endpoint

import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Create the data model
# The data model describes the format of the input and output data
# The model is a simple dictionary with two fields: sepal_length, sepal_width

class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    
# 2. Load the model
# The model is a serialized scikit-learn model

with open('model.pkl', 'rb') as f:
    model = joblib.load(f)
    

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 3. Create the health check endpoint
# The health check endpoint is used to check if the server is up and running

@app.get("/health")
async def health():
    return {"status": "ok"}

# 4. Create the prediction endpoint
# The prediction endpoint is used to get predictions from the model

@app.post("/predict")
async def predict(data: IrisData):
    data = data.dict()
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    prediction = model.predict([[sepal_length, sepal_width]])[0]
    return {
        'prediction': prediction
    }