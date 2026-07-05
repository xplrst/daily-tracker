@echo off
:: Sets a clean title for your command prompt window
title Python Script Runner

:: Navigate to your script folder
cd /d "%USERPROFILE%\Documents\Notes\Daily Tracker\Script"

echo Launching your Python script...
echo -----------------------------------
clc
:: Execute your script (replace 'your_script.py' with your actual filename)
python generate_daily_tracker.py

echo -----------------------------------
echo Script execution finished.
pause
