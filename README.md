[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LOuMvgtV)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11507333&assignment_repo_type=AssignmentRepo)
# MAST30034 Project 1 README.md
- Name: `Di Wu`
- Student ID: `1208784`

**Research Goal:** My research goal is to explore the dymanic pricing system used by FHV companies, to optimise drivers earning. 

**Timeline:** The timeline for the research area is January 2022 - March 2023

To run the pipeline, run the files in order:
1. `Download.py` from `scripts` directory: This downloads the raw data into the `data/landing` directory.
2. `DataEngineering.ipynb` from `notebooks` directory: This notebook details all preprocessing and data engineering steps for all datasets and outputs it to the `data/raw` and `data/curated` directory.
3. `DataVisualization.ipynb` from `notebooks` directory: This notebook is used to conduct analysis with visualisation on the curated data.
4. `Query.ipynb` from `notebooks` directory: This notebook simply runs query on the aggregated data for the information required in model analysis. 
5. `Model.ipynb` from `notebooks` directory: The notebook is used to build the Linear Regression and Random Forest Regressor models, with analysing conducted. 
