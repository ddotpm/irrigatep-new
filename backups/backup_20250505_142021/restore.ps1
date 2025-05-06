[CmdletBinding()]
param()

try {
    $sourceDir = $PSScriptRoot
    $destDir = (Resolve-Path -Path (Join-Path -Path $PSScriptRoot -ChildPath "..")).Path

    Write-Host "Restoring from: $sourceDir"
    Write-Host "Restoring to: $destDir"

    Get-ChildItem -Path $sourceDir -Exclude "restore.ps1" | ForEach-Object {
        $destPath = Join-Path -Path $destDir -ChildPath $_.Name
        Copy-Item -Path $_.FullName -Destination $destPath -Recurse -Force
        Write-Host "Restored: $($_.Name)"
    }

    Write-Host "Restore completed successfully" -ForegroundColor Green
}
catch {
    Write-Error "Restore failed: $_"
    exit 1
}
