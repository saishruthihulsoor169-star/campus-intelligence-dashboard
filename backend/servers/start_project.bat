@echo off
cd backend
start cmd /k "uvicorn main:app --port 8001"