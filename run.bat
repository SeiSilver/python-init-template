@echo off
echo --- Initializing Python Template ---

:: Check if uv is installed, otherwise fallback to standard python
where uv >nul 2>1
if %errorlevel% == 0 (
    echo Using 'uv' for faster execution...
    if not exist .venv (
        uv venv
    )
    uv pip install -r requirements.txt
    uv run python src/main.py
) else (
    echo 'uv' not found, falling back to standard venv...
    if not exist .venv (
        python -m venv .venv
    )
    call .venv\Scripts\activate
    pip install -r requirements.txt
    python src/main.py
)

pause