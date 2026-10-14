# Machine Learning & AI Development Environment

This repository contains a pre-configured Python environment tailored for Machine Learning, Deep Learning, Data Science, and Kaggle competitions.

---

## 📦 Installed Libraries & Tooling

| Category | Libraries / Tools | Description |
| :--- | :--- | :--- |
| **Data Processing & Math** | `numpy`, `pandas`, `scipy` | High-performance array operations, dataframes, and scientific computing. |
| **Data Visualization** | `matplotlib`, `seaborn` | Static, animated, and interactive statistical plots and charts. |
| **Classical Machine Learning**| `scikit-learn` | Regression, classification, clustering, preprocessing, and model evaluation metrics. |
| **Deep Learning Frameworks** | `tensorflow`, `torch`, `torchvision` | State-of-the-art neural network modeling and computer vision. |
| **Kaggle API** | `kaggle` | Official CLI tool to search, download datasets, and submit competition entries. |
| **Interactive Computing** | `ipykernel`, `notebook` | Jupyter notebook and kernel support for interactive exploration. |

---

## 🚀 Quick Start Guide

### ⚡ Quick Copy & Paste (TL;DR)

Choose your shell below to activate the environment (`.venv`) and install requirements:

#### Windows PowerShell
```powershell
# 1. Activate the environment (note the dot-backslash and .ps1 extension)
.\.venv\Scripts\Activate.ps1

# 2. Install packages from requirements.txt
pip install -r requirements.txt

# 3. Verify installation
python verify_env.py
```

#### Windows Command Prompt (CMD)
```cmd
:: 1. Activate the environment
.venv\Scripts\activate.bat

:: 2. Install packages from requirements.txt
pip install -r requirements.txt

:: 3. Verify installation
python verify_env.py
```

#### macOS / Linux / Git Bash
```bash
# 1. Activate the environment
source .venv/bin/activate

# 2. Install packages from requirements.txt
pip install -r requirements.txt

# 3. Verify installation
python verify_env.py
```

---

### 1. Prerequisites
- **Python**: Recommended version **3.10 - 3.12** for broad compatibility across PyTorch and TensorFlow.

---

### 2. Create the Virtual Environment

Run one of the following commands in your project root directory (you can name the environment `env` or `.venv`):

#### Windows (PowerShell or Command Prompt)
```powershell
# Using Python launcher (recommended if you have multiple Python versions):
py -3.12 -m venv env

# Or using the default python command:
python -m venv env
```

#### macOS / Linux
```bash
python3 -m venv env
```

> **Note:** If you prefer using `.venv` instead of `env`, replace `env` with `.venv` in the commands above and below. Both folder names are already configured in `.gitignore`.

---

### 3. Activate the Virtual Environment

Before installing packages or running scripts, activate the virtual environment in your terminal:

#### ⚡ Windows PowerShell
```powershell
# If your environment folder is named 'env':
.\env\Scripts\Activate.ps1

# If your environment folder is named '.venv':
.\.venv\Scripts\Activate.ps1
```

> **PowerShell Script Execution Policy Error Fix:**  
> If you see `File ... cannot be loaded because running scripts is disabled on this system`, enable script execution for your current PowerShell session:
> ```powershell
> Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
> .\env\Scripts\Activate.ps1
> ```

#### 💻 Windows Command Prompt (CMD)
```cmd
:: If your environment folder is named 'env':
env\Scripts\activate.bat

:: If your environment folder is named '.venv':
.venv\Scripts\activate.bat
```

#### 🐧 Git Bash / Linux / macOS
```bash
# For Git Bash on Windows:
source env/Scripts/activate

# For Linux / macOS:
source env/bin/activate
```

> **Tip:** When the environment is successfully activated, your terminal prompt will show `(env)` or `(.venv)` at the beginning of the line.

---

### 4. Install Dependencies from `requirements.txt`

Once the virtual environment is active, install or update all required packages:

```bash
# Step A: Upgrade pip to the latest version
python -m pip install --upgrade pip

# Step B: Install all packages from requirements.txt
pip install -r requirements.txt
```

> **Tip for pre-compiled wheels:** You can also use `pip install --prefer-binary -r requirements.txt` to speed up installation by avoiding source compilation where possible.

---

### 5. Verify Your Environment

Test that all libraries (NumPy, Pandas, PyTorch, TensorFlow, etc.) are installed and functional:

#### Option A: Run the Verification Script (Recommended)
```bash
python verify_env.py
```

#### Option B: Quick One-Liner Check
```bash
python -c "import numpy as np, pandas as pd, matplotlib, sklearn, tensorflow as tf, torch; print('All ML/DL packages imported successfully!'); print('TensorFlow version:', tf.__version__); print('PyTorch version:', torch.__version__); print('CUDA Available for Torch:', torch.cuda.is_available())"
```

---

### 6. Using with Jupyter Notebooks / VS Code

To make your virtual environment available as a Jupyter kernel in VS Code or Jupyter Notebook:

```bash
python -m ipykernel install --user --name=ml-env --display-name="Python (Machine Learning)"
```

When opening any `.ipynb` notebook in VS Code, click **"Select Kernel"** at the top right and choose **"Python (Machine Learning)"** or your active virtual environment (`env` / `.venv`).

---

### 7. Setting Up Kaggle API

1. Go to your account settings on [kaggle.com](https://www.kaggle.com).
2. Click **"Create New Token"** to download `kaggle.json`.
3. Place `kaggle.json` in the default directory:
   - **Windows:** `C:\Users\<Your-Username>\.kaggle\kaggle.json`
   - **Linux / macOS:** `~/.kaggle/kaggle.json`
4. Test access:
   ```bash
   kaggle datasets list -s "titanic"
   ```

---

### 8. How to Deactivate the Environment

When you are done working, exit the virtual environment:

```bash
deactivate
```
