# 🐍 Pexels Image & Video Downloader

A simple Python tool to **download images and videos** from [Pexels](https://www.pexels.com) using their public API.  
Each keyword gets its own folder under `/output`, containing downloaded images and videos.

This project uses [**uv**](https://github.com/astral-sh/uv) — a fast, modern Python package and environment manager.

---

## 🚀 Features

- Download both **images** and **videos** for a list of keywords.
- **Multi-threaded downloads** for faster parallel processing.
- Configurable limits via `.env` file.

- Easy setup with `uv` (no manual `venv` or `pip` commands needed).

---

## 🧩 Prerequisites

- Python **3.9+**
- A [Pexels API key](https://www.pexels.com/api/new/)
- `uv` installed

### Install `uv`

#### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows (PowerShell)

```powershell
winget install --id=astral-sh.uv  -e
```

## 🔧 Configuration

Create a `.env` file in the project root with your API key and limits:

```env
PEXELS_API_KEY=YOUR_PEXELS_API_KEY
IMAGE_LIMIT=5
VIDEO_LIMIT=3
MAX_WORKERS=5
```

- `MAX_WORKERS`: Number of parallel download threads (default: 5). Increase for faster downloads, but be mindful of API rate limits.

You can modify the code to load from a file `keywords.txt` if needed.

---

## 🏃 Run the tool

### Windows (Easiest)
Double-click `run.bat` or run:
```batch
run.bat
```

### Manual Run
```bash
uv venv
uv pip install -r requirements.txt
uv run python -m src.main
```

OR (with auto-install dependencies)
```bash
uv run --with requirements.txt python -m src.main
```

## References

* [uv by Astral](https://github.com/astral-sh/uv)
