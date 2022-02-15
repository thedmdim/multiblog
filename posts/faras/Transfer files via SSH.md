# SCPP
# SCPP2
## SCP
```bash
scp [source username@IP]:/[directory and file name] [destination username@IP]:/[destination directory]
```
Example. A file from linux to windows:
```bash
scp root@161.97.155.161:/root/myfile.txt C:\Users\lu\Desktop\
```
Example. A folder from linux to windows `-r` key:
```bash
scp -r root@161.97.155.161:/root/mydir C:\Users\lu\Desktop\
```
