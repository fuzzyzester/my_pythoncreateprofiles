# Python Create Profiles with CICD and GitHub Pages

## Overview
This project showcases a complete CI/CD workflow, data generation, conversion, and testing pipeline using Python, GitHub Actions, and GitHub Pages. It fulfills all the requirements for a VG grade.

## Features Implemented
- **Branch Management:**
  - Separate branches for each feature:
    - `feature/tests` for testing code  
    - `feature/csvtojson` for CSV to JSON conversion  
    - `feature/cicd` for CI/CD pipeline setup  
  - Branches merged into `main` with meaningful commits.

- **Data Generation:**
  - `generate.py` uses `faker` to create realistic profile data in `profiles1.csv`.

- **CSV to JSON Conversion:**
  - `csvtojson.py` converts `profiles1.csv` into `data.json`.

- **Automated Testing:**
  - `run_tests.py` (including `test_csvtojson.py`) verifies:
    - CSV has 12 columns.
    - CSV has 900+ rows.
    - JSON has correct properties.
    - JSON has 900+ rows.

- **CI/CD Pipeline:**
  - Workflow triggered on pushes and pull requests to `main`.
  - Steps:
    - Checkout code.
    - Setup Python and install dependencies (`pytest`, `faker`).
    - Run `generate.py` to create CSV.
    - Run `csvtojson.py` to convert to JSON.
    - Run tests to validate CSV and JSON.
    - Copy `index.html`, `script.js`, and `data.json` to `dist/`.
    - Deploy the content to GitHub Pages.

- **GitHub Pages Deployment:**
  - Automatic deployment of the `dist/` folder to GitHub Pages.


