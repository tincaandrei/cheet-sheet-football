## Soccerdata Notebook Setup

This project contains Jupyter notebooks that use the [`soccerdata`](https://pypi.org/project/soccerdata/) package (FBref) to scrape and analyze football data.

### 1. Clone the repo

```bash
git clone https://github.com/tincaandrei/cheet-sheet-football.git
cd Soccerdata
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Jupyter / VS Code

**Jupyter Lab / Notebook:**

```bash
jupyter lab
# or
jupyter notebook
```

Then open `scraper.ipynb` and select the `venv` Python kernel.

**VS Code:**

- Open the folder in VS Code.
- Select the `venv` Python interpreter.
- Open `scraper.ipynb` and run the cells.

### 5. Updating dependencies

If you install new packages and want to share them, update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

