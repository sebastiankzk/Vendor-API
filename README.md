# Setup and Run the Project

## 1. Create a Virtual Environment

Open Command Prompt, navigate to the root directory of the project, and run the following command to create a virtual environment:

```bash
python -m venv .venv
```

## 2. Install required packages

```bash
pip install -r requirements.txt
```
there should be a (.venv) showing before the directory location

## 3. Start application

```bash
uvicorn main:app --reload
```
