# SSH Cheatsheet

## Create SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

## Add private key to SSH agent
```bash
eval "$(ssh-agent -s)"  # Start the SSH agent
ssh-add ~/.ssh/id_ed25519  # Add the private key
```
## Install ssh-copy-id
On debian based systems, you can install `ssh-copy-id` using the following command:
```bash
sudo apt install openssh-client
```
On macOS, `ssh-copy-id` is included with the SSH client by default.

## Copy public key to remote server
```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote_host
```
