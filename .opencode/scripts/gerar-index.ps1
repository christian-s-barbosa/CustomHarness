param(
  [Parameter(Mandatory = $true)][string]$VaultPath,
  [string]$OutFile = "index.md",
  [string]$Titulo = "Índice"
)

$VaultPath = (Resolve-Path -LiteralPath $VaultPath).Path
$excludeDirs = @(".obsidian", "templates")
$outPath = Join-Path $VaultPath $OutFile

$files = Get-ChildItem -LiteralPath $VaultPath -Recurse -File -Filter *.md |
  Where-Object {
    $rel = $_.FullName.Substring($VaultPath.Length + 1)
    $parts = $rel -split '[\\/]'
    ($parts[0] -notin $excludeDirs) -and ($rel -ne $OutFile)
  }

$lines = @()
$lines += "---"
$lines += "tipo: index"
$lines += "atualizado: " + (Get-Date -Format "yyyy-MM-dd")
$lines += "---"
$lines += ""
$lines += "# $Titulo"
$lines += ""

$groups = $files | Group-Object {
    $rel = $_.FullName.Substring($VaultPath.Length + 1)
    $parts = $rel -split '[\\/]'
    if ($parts.Count -le 1) { "." }
    elseif ($parts[0] -eq "historico") {
      if ($parts.Count -ge 3 -and $parts[1] -match '^\d{4}$') { "historico/$($parts[1])/$($parts[2])" }
      else { "historico/$($parts[1])" }
    }
    else { $parts[0] }
  } | Sort-Object Name

foreach ($g in $groups) {
  $nome = if ($g.Name -eq ".") { "Raiz" } else { $g.Name }
  $lines += "## $nome"
  foreach ($f in ($g.Group | Sort-Object FullName)) {
    $rel = ($f.FullName.Substring($VaultPath.Length + 1)) -replace '\\', '/'
    $link = $rel -replace '\.md$', ''
    $lines += "- [[$link|$($f.BaseName)]]"
  }
  $lines += ""
}

Set-Content -LiteralPath $outPath -Value ($lines -join "`n") -Encoding UTF8
Write-Output "index gerado: $outPath ($($files.Count) notas)"
