call venv\Scripts\activate.bat
uvicorn main:app --host 192.168.178.37 --port 8000 --reload
call venv\Scripts\deactivate.bat