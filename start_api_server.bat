@echo off
echo Starting ComputerService FastAPI server...
uvicorn api:app --reload
pause