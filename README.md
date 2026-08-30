## Automated-VSCode-Extensions-Export-and-Import

Script for automated vscode extensions export and import

#### Get the List of Installed VSCode Extensions (On Linux / macOS / Windows (Git Bash, WSL, or any bash-like shell)):

```
code --list-extensions > vscode-extensions.txt
```

#### Install VSCode Extensions List from the vscode-extensions.txt file

- Windows (PowerShell)

```
Get-Content vscode-extensions.txt | ForEach-Object { code --install-extension $_ }
```

👉 Add --force if you want to reinstall/update:

```
Get-Content vscode-extensions.txt | ForEach-Object { code --install-extension $_ --force }
```

- macOS / Linux (bash, zsh, sh, etc.)

```
xargs -n 1 code --install-extension < vscode-extensions.txt
```

👉 With --force (reinstall/update):

```
xargs -n 1 code --install-extension --force < vscode-extensions.txt
```

#### Install VSCode Extensions List from the vscode-extensions.txt file using bash scripting

- Create a file with `install-extensions.sh` name.
- Paste the below content in the file & save it:

```
#!/bin/bash
while read extension; do
    echo "Installing: $extension"
    code --install-extension "$extension" --force
    echo "-----------------------------------"
done < vscode-extensions.txt
```

- Make it executable: `chmod +x install-extensions.sh`

- Run it: `./install-extensions.sh`

#### Download the VSIX format of VSCode extensions (Using Python script):

- Download dependencies:

```
pip install requests
```

- Run python script:

```
python downloadextensions.py
```

---

## Cursor

The same workflow works for Cursor — its CLI mirrors the `code` CLI, just replace `code` with `cursor`.

> **Note:** If the `cursor` command is not found, open Cursor, press `Cmd/Ctrl + Shift + P` and run **"Shell Command: Install 'cursor' command"**.

#### Get the List of Installed Cursor Extensions (On Linux / macOS / Windows (Git Bash, WSL, or any bash-like shell)):

```
cursor --list-extensions > vscode-extensions.txt
```

#### Install Cursor Extensions List from the vscode-extensions.txt file

- Windows (PowerShell)

```
Get-Content vscode-extensions.txt | ForEach-Object { cursor --install-extension $_ }
```

👉 Add --force if you want to reinstall/update:

```
Get-Content vscode-extensions.txt | ForEach-Object { cursor --install-extension $_ --force }
```

- macOS / Linux (bash, zsh, sh, etc.)

```
xargs -n 1 cursor --install-extension < vscode-extensions.txt
```

👉 With --force (reinstall/update):

```
xargs -n 1 cursor --install-extension --force < vscode-extensions.txt
```

#### Install Cursor Extensions List from the vscode-extensions.txt file using bash scripting

- Create a file with `install-cursor-extensions.sh` name.
- Paste the below content in the file & save it:

```
#!/bin/bash
while read extension; do
    echo "Installing: $extension"
    cursor --install-extension "$extension" --force
    echo "-----------------------------------"
done < vscode-extensions.txt
```

- Make it executable: `chmod +x install-cursor-extensions.sh`

- Run it: `./install-cursor-extensions.sh`

#### Reuse your VSCode extensions list in Cursor

Since Cursor uses the same extension IDs as the VSCode Marketplace, you can install the extensions from the existing `vscode-extensions.txt` file directly:

```
xargs -n 1 cursor --install-extension < vscode-extensions.txt
```

#### Install downloaded VSIX files in Cursor

The VSIX files downloaded with the Python script above can also be installed in Cursor:

```
cursor --install-extension vsix_files/<extension-id>.vsix
```
