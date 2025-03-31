# Prefix Calculator
<br>

### Author  
**By Shreeyukta Pradhanang**  
**Student ID: st125168**

<br>

This is a GUI-based prefix calculator built using **Python 3.9** and **PyQt6** for the **Programming Language and Compiler course at AIT**. It supports prefix arithmetic expressions using `+` and `*`, evaluates the result, and shows the equivalent infix notation.

---

## What This App Does

- Accepts **prefix expressions** (e.g., `+ * 2 3 4`)
- Evaluates the expression result
- Displays the equivalent **infix** expression (e.g., `((2 * 3) + 4)`)
- GUI built with **PyQt6** and **Qt Designer**

---

## How to Clone and Use

### Clone the Project

```bash
git clone https://github.com/shreeyukta/calculator-plc.git
cd calculator-plc
```

---

## Run the App

You can either run it locally using [PDM](https://pdm-project.org) or inside a Docker container.

### Option 1: Run Locally (Recommended for Simplicity)

> Make sure Python 3.9 and PDM are installed

```bash
pdm install          # install dependencies
pdm run app          # launch the calculator GUI
```

### Option 2: Run with Docker (Optional)

> Requires Docker and optionally XQuartz/X410 if you want GUI inside container

1. Clone the repo
2. Open in VSCode and select **Dev Containers: Reopen in Container**
3. Inside the container, run:

```bash
pdm install
pdm run app
```

---

## UI Tools

- GUI was built with **Qt Designer 6**
- To edit the UI manually:

```bash
pdm shell pyqt6-tools designer
```

---

## Folder Structure

```
compiler-starter-project/
  ├─ components/
  │   ├─ ast/
  │   ├─ lexica.py
  │   ├─ main.ui
  │   ├─ memory.py
  │   └─ parsers.py
  └─ main.py
```

---

> Created as a learning project for parsing, GUI design, and prefix expression evaluation using Python.
