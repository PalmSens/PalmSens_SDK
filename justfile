set windows-shell := ['powershell.exe', '-NoProfile', '-NoLogo', '-Command']

# use print to capture result of evaluation
list_version *ARGS:
    uv run tools/version.py {{ARGS}}
