param(
    [int]$workers = 12,
    [string]$output = "output_max_speed",
    [switch]$background
)

Write-Host "🚀 MAXIMUM SPEED FLUTE OPTIMIZATION" -ForegroundColor Green
Write-Host "Using $workers CPU cores" -ForegroundColor Yellow
Write-Host "Output directory: $output\" -ForegroundColor Cyan
Write-Host ""

$arguments = @(
    "run_flute.py",
    $output,
    "--workers", $workers.ToString(),
    "--transpose", "12"
)

if ($background) {
    Write-Host "Starting in background mode..." -ForegroundColor Magenta
    Start-Process -FilePath "python" -ArgumentList $arguments -NoNewWindow -Priority "High"
    Write-Host "Process started! Check Task Manager for CPU usage." -ForegroundColor Green
} else {
    Write-Host "Starting optimization..." -ForegroundColor Green
    & python $arguments
}

Write-Host ""
Write-Host "Results will be saved to: $output\" -ForegroundColor White -BackgroundColor Blue
