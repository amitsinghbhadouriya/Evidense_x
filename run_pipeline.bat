@echo off
echo ========================================================
echo Evidense-X End-to-End Pipeline Reproduction Runner
echo ========================================================

echo Step 1: Running unit tests...
pytest tests/ -v
if %ERRORLEVEL% NEQ 0 exit /b %ERRORLEVEL%

echo Step 2: Generating summary tables...
python generate_summary_tables.py

echo Step 3: Generating publication figures...
python analyze_and_plot.py

echo Pipeline completed successfully!
