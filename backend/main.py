from fastapi import FastAPI
import random
from ai_models import predict_risk

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Construction System Running"}

@app.get("/predict_risk")
def risk_analysis():
    return {"project_risk": predict_risk()}

@app.get("/equipment_status")
def equipment_status():
    return {"failure_expected": bool(random.randint(0, 1))}

@app.get("/material_optimization")
def material_optimization():
    return {"optimized_materials": {"cement": random.randint(50, 200), "steel": random.randint(20, 100)}}
