@echo off
echo ========================================
echo MAXIMUM SPEED FLUTE OPTIMIZATION
echo Using ALL available CPU cores (12)
echo ========================================
echo.

REM Запуск с максимальным приоритетом и всеми ядрами
start /HIGH /B python run_flute.py output_max_speed --workers 12 --transpose 12

echo Process started with HIGH priority!
echo Using 12 CPU cores for maximum speed
echo Results will be saved to: output_max_speed\
echo.
echo Press any key to exit (process continues in background)
pause > nul
