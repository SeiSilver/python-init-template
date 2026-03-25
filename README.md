# 🐍 Python Project Template

A clean, modular starter template for Python projects. This structure is designed to be scalable, using a dedicated
`service` layer and a centralized `config` for environment management.

---

## 📂 Project Structure

```text
python-init-template/
├── input/              # Default directory for local files/data
├── src/
│   ├── service/        # Business logic and external API services
│   │   └── test_service.py
│   ├── config.py       # Centralized configuration & path management
│   └── main.py         # Entry point
├── .env                # Environment variables (API keys, settings)
├── requirements.txt    # Project dependencies
└── run.bat             # Quick-start script for Windows
```

## 🚀 Features

- **Modular Design:** Logic is separated into services to keep `main.py` clean.
- **Environment Management:** Pre-configured with `python-dotenv` for security.
- **Path Safety:** Automatic folder creation (e.g., `/input`) via `config.py`.
- **Essential Toolkit:** Includes `requests`, `tqdm` for progress bars, and `Pillow` for image processing.

---

## 🔧 Setup

1. **Install Dependencies**
   If you are using `uv`:
   ```bash
   uv pip install -r requirements.txt
   ```
   Or using standard `pip`:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   Create a `.env` file in the root directory:
   ```env
   APP_NAME=MyPythonProject
   DEBUG=True
   # Add your API keys below
   ```

---

## 🏃 How to Run

### Windows (Recommended)

Simply double-click `run.bat` or run:

```batch
run.bat
```

### Manual Run

Ensure your virtual environment is active, then run:

```bash
python src/main.py
```

---

## 📦 Included Libraries

| Library           | Purpose                                  |
|:------------------|:-----------------------------------------|
| **requests**      | Making HTTP/API calls.                   |
| **python-dotenv** | Managing configuration via `.env` files. |