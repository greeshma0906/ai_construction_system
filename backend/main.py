import os
import random
import pandas as pd
from fastapi import FastAPI, File, UploadFile
from ai_models import predict_risk

app = FastAPI()

#  Manually set the path for uploaded CSV files
UPLOAD_DIR = "uploaded_files"
CSV_FILE_PATH = os.path.join(UPLOAD_DIR, "current_data.csv")

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

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
    return {
        "optimized_materials": {
            "cement": random.randint(50, 200),
            "steel": random.randint(20, 100)
        }
    }

#  API to Upload Current Data CSV
@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        #  Save the uploaded file at a fixed location
        with open(CSV_FILE_PATH, "wb") as f:
            f.write(file.file.read())

        #  Read Current Data CSV
        df_current = pd.read_csv(CSV_FILE_PATH)

        #  Generate Larger Past Data for Analysis (100 records)
        num_past_records = 100
        past_data = {
            "risk_level": [random.uniform(0.4, 0.9) for _ in range(num_past_records)],
            "equipment_status": [random.choice([0, 1]) for _ in range(num_past_records)],
            "optimized_cement": [random.randint(100, 200) for _ in range(num_past_records)],
            "optimized_steel": [random.randint(50, 100) for _ in range(num_past_records)],
        }
        df_past = pd.DataFrame(past_data)

        #  Compare Current vs Past Data
        comparison = df_current.mean() - df_past.mean()

        return {
            "message": "CSV uploaded and processed successfully",
            "comparison_result": comparison.to_dict()
        }
    except Exception as e:
        return {"error": str(e)}
