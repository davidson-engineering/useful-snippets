# Network Drives, Mounting and Unmounting
keywords: network drives, mount, unmount, samba, cifs, nfs

## Mounting a Network Drive

Create a directory to mount the network drive:
```bash
(sudo) mkdir /mnt/mountpoint
```
### Mounting an NFS Share
NFS (Network File System) is a protocol used to share files over a network. To mount an NFS share, you need to have the `nfs-common` package installed. You can install it using:
```bash
sudo apt-get install nfs-common
```
Then, you can mount the NFS share using the following command:
```bash
sudo mount -t nfs server:/path/to/share /mnt/mountpoint
```
### Mounting an SMB/CIFS Share
SMB/CIFS (Server Message Block/Common Internet File System) is a protocol used for sharing files and printers. To mount an SMB/CIFS share, you need to have the `cifs-utils` package installed. You can install it using:
```bash
sudo apt-get install cifs-utils
```
Then, you can mount the SMB/CIFS share using the following command:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o username=user,password=pass
```

### Mounting a Samba Share
Samba is an open-source implementation of the SMB/CIFS protocol. To mount a Samba share, you can use the same command as for SMB/CIFS:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o username=user,password=pass
```
### Credentials File
Instead of passing the username and password in the command line, you can create a credentials file to store them securely. Create a file (e.g., `~/.smbcredentials`) with the following content:
```bash
echo "username=user" > ~/.smbcredentials
echo "password=pass" >> ~/.smbcredentials
```
Then, change the permissions of the file to make it readable only by you:
```bash
chmod 600 ~/.smbcredentials
```
Now, you can mount the share using the credentials file:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o credentials=/path/to/.smbcredentials
```
### Mounting with Options
You can also specify additional options when mounting a network drive. For example, to mount a CIFS share with read-only access, you can use:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o username=user,password=pass,ro
```
### Mounting with UID and GID
You can specify the user ID (UID) and group ID (GID) for the mounted share. This is useful if you want to set specific permissions for the mounted files. You can do this using the `uid` and `gid` options:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o username=user,password=pass,uid=1000,gid=1000
```
### Mounting with File Permissions
You can also specify file permissions for the mounted share using the `file_mode` and `dir_mode` options. For example, to set the file permissions to `0644` and directory permissions to `0755`, you can use:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o username=user,password=pass,file_mode=0644,dir_mode=0755
```
### Mounting with Timeouts
You can specify timeouts for the mount operation using the `soft` and `hard` options. The `soft` option will cause the mount to fail after a certain number of retries, while the `hard` option will keep retrying indefinitely. For example:
```bash
sudo mount -t cifs //server/share /mnt/mountpoint -o username=user,password=pass,soft,retry=3
```

