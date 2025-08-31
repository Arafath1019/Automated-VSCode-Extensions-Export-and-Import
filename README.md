## Automated-VSCode-Extensions-Export-and-Import
Script for automated vscode extensions export and import

#### Get the List of Installed VSCode Extensions (On Linux / macOS / Windows (Git Bash, WSL, or any bash-like shell)):
```
code --list-extensions > vscode-extensions.txt
```

#### Install VSCode Extensions List from the vscode-extensions.txt file
* Windows (PowerShell)
```
Get-Content vscode-extensions.txt | ForEach-Object { code --install-extension $_ }
```
👉 Add --force if you want to reinstall/update:
```
Get-Content vscode-extensions.txt | ForEach-Object { code --install-extension $_ --force }
```

* macOS / Linux (bash, zsh, sh, etc.)
```
xargs -n 1 code --install-extension < vscode-extensions.txt
```
👉 With --force (reinstall/update):
```
xargs -n 1 code --install-extension --force < vscode-extensions.txt
```

#### Download the VSIX format of VSCode extensions (Using Python script):
* Download dependencies:
```
pip install requests
```

* Run python script:
```
python downloadextensions.py
```