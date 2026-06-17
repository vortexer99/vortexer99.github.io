$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$pythonCandidates = @(
  "python",
  "py",
  "$env:LOCALAPPDATA\Python\bin\python.exe"
)

$python = $null
foreach ($candidate in $pythonCandidates) {
  try {
    $command = Get-Command $candidate -ErrorAction Stop
    $python = $command.Source
    break
  } catch {
    continue
  }
}

if (-not $python) {
  throw "Python was not found. Install Python 3.10+ and PySide6, then rerun this script."
}

Set-Location $repoRoot
& $python -B tools\site_manager.py
