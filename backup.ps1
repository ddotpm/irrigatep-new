# Backup script for IrrigateP project
[CmdletBinding()]
param()

function New-ProjectBackup {
    [CmdletBinding()]
    param (
        [Parameter()]
        [string]$RootPath = $PSScriptRoot
    )

    try {
        # Get current timestamp for backup name
        $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
        $backupDir = Join-Path -Path $RootPath -ChildPath "backups"
        $backupName = "backup_$timestamp"
        $currentBackupDir = Join-Path -Path $backupDir -ChildPath $backupName

        # Create backup directories
        Write-Verbose "Creating backup directory: $backupDir"
        $null = New-Item -ItemType Directory -Path $backupDir -Force
        $null = New-Item -ItemType Directory -Path $currentBackupDir -Force

        # Define items to backup
        $itemsToBackup = @(
            (Join-Path -Path $RootPath -ChildPath "apps"),
            (Join-Path -Path $RootPath -ChildPath "docker-compose.yml"),
            (Join-Path -Path $RootPath -ChildPath "dev.sh")
        )

        # Copy items to backup directory
        foreach ($item in $itemsToBackup) {
            if (Test-Path -Path $item) {
                Write-Verbose "Backing up: $item"
                $destPath = Join-Path -Path $currentBackupDir -ChildPath (Split-Path -Path $item -Leaf)
                Copy-Item -Path $item -Destination $destPath -Recurse -Force
            }
            else {
                Write-Warning "Item not found: $item"
            }
        }

        # Create restore script
        $restoreScriptPath = Join-Path -Path $currentBackupDir -ChildPath "restore.ps1"
        $restoreScript = @'
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
'@
        Set-Content -Path $restoreScriptPath -Value $restoreScript

        Write-Host "Backup created successfully at: $currentBackupDir" -ForegroundColor Green
        Write-Host "To restore, run: .\restore.ps1 from the backup directory" -ForegroundColor Yellow
    }
    catch {
        Write-Error "Backup failed: $_"
        exit 1
    }
}

# Execute backup
New-ProjectBackup -Verbose 