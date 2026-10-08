# Linux Homework

## Task 1: Soft Link and Hard Link

### Soft Link

Command:

```bash
echo "Hello Linux" > original.txt
ln -s original.txt softlink.txt
ls -li
```

A soft link is a separate file that points to the path of another file.

### Hard Link

Command:

```bash
ln original.txt hardlink.txt
ls -li
```

The original file and hard link have the same inode number because they point to the same underlying file data.

### Difference

| Soft Link                   | Hard Link                                     |
| --------------------------- | --------------------------------------------- |
| Uses a file path            | Points to the same inode                      |
| Different inode             | Same inode                                    |
| Can cross filesystems       | Must be on the same filesystem                |
| Breaks if target is deleted | Continues to work if another hard link exists |

---

## Task 2: adduser vs useradd

`useradd` is a lower-level utility for creating users.

`adduser` is a more user-friendly wrapper that simplifies user creation and account setup.

On Ubuntu, `adduser` is generally preferred for interactive user creation, while `useradd` is useful for scripting and automation.

### Test user

```bash
sudo adduser testuser
id testuser
getent passwd testuser
```

The test user was successfully created and verified.

---

## Task 3: journalctl

`journalctl` is used to view logs collected by systemd's journal.

### View recent logs

```bash
sudo journalctl -n 20
```

### View logs from the current boot

```bash
sudo journalctl -b
```

### View logs for a specific service

```bash
sudo journalctl -u ssh -n 20
```

### Follow logs in real time

```bash
sudo journalctl -f
```

`journalctl` is useful for troubleshooting services, system errors, boot problems, and application issues.

---

## Task 4: Linux Command Cheat Sheet

### Navigation

```bash
pwd
ls
ls -la
cd
cd ..
```

### File management

```bash
touch
mkdir
cp
mv
rm
```

### File viewing

```bash
cat
less
head
tail
```

### Searching

```bash
grep
find
```

### Permissions

```bash
chmod
chown
```

### Processes

```bash
ps
top
kill
```

### Networking

```bash
ip addr
ping
curl
ss
```

### Disk usage

```bash
df -h
du -sh
```

### System information

```bash
uname -a
whoami
hostname
free -h
```

These commands were practiced to understand basic Linux navigation, file management, permissions, process management, networking, system information, and log management.