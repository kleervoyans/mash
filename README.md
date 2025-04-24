# Mash

Automatically generate a concise Markdown product sheet (“one-pager”) for any public GitHub repository.

## Features
- Project overview
- Build & run instructions
- License summary
- Known issues (top 5 open)
- Multilingual support (EN, DE, TR)

## Installation
```bash
pip install -r requirements.txt
```

## Setup
1. Create `.env` with:
```bash
GITHUB_TOKEN=your_github_token_here
```
2. Run CLI:
```bash
python mash.py https://github.com/kleervoyans/mash
```
3. Or launch web demo:
```bash
streamlit run app.py
```
