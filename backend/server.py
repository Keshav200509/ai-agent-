# from fastapi import FastAPI
# from agent.core import run_agent

# app = FastAPI()

# @app.post("/run-agent")
# def run_agent_endpoint(task: str):
#     result = run_agent(task)
#     return {"result": result}


from fastapi import FastAPI, HTTPException
from agent.core import run_agent_task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Educational AI Agent is running!"}

@app.post("/run")
def run_agent(query: str):
    try:
        response = run_agent_task(query)
        return {"result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
