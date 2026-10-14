Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Evidense-X End-to-End Pipeline Reproduction Runner" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan

Write-Host "Step 1: Running unit tests..." -ForegroundColor Green
pytest tests/ -v
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "Step 2: Generating summary tables..." -ForegroundColor Green
python generate_summary_tables.py

Write-Host "Step 3: Generating publication figures..." -ForegroundColor Green
python analyze_and_plot.py

Write-Host "Pipeline completed successfully!" -ForegroundColor Cyan
