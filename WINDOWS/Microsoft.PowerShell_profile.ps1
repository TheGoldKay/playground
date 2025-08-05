function jackett {
    Start-Process msedge "http://127.0.0.1:9117/UI/Dashboard"
}

function pyenv {
    .venv/Scripts/activate
}

function run { 
    uv run python @args 
}

# run fastfetch at startup
fastfetch

# alias which=get-command
New-Alias -Name which -Value Get-Command

