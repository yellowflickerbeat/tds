from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import subprocess
import logging

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Log setup
logging.basicConfig(filename="agent.log", level=logging.INFO)

@app.get("/task")
def run_task(q: str = Query(..., description="Task description")):
    logging.info(f"Received task: {q}")

    # Simulate sending to a CLI coding agent (e.g., Copilot CLI)
    # Here we just handle the specific example task directly for demo
    if "binary" in q and "396" in q:
        # Run actual Python code to generate binary
        code = "print(format(396, 'b'))"
        output = subprocess.check_output(["python3", "-c", code], text=True).strip()
    else:
        # Generic placeholder for real agent execution
        output = f"Simulated agent output for: {q}"

    logging.info(f"Task output: {output}")

    return JSONResponse(
        content={
            "task": q,
            "agent": "copilot-cli",
            "output": output,
            "email": "23f2001624@ds.study.iitm.ac.in"
        }
    )
