# Shell Scripting: System Information

`system_info.sh` prints basic system information and saves the current process list in a file.

## Run the script

```bash
chmod +x system_info.sh
./system_info.sh
```

## Input

The script asks for a directory name. For example:

```text
Enter a directory name: sample_output1
```

It creates the directory and writes the process list to `sample_output1/processes.txt`.

## Output

The terminal output includes:

```text
===== SYSTEM INFORMATION =====
Date: <current date>
Hostname: <computer name>
Username: <current user>

===== DISK USAGE =====
<df -h output>

===== RUNNING PROCESSES =====
<ps output>

Running processes have been saved to sample_output1/processes.txt
```

View the saved output with:

```bash
cat sample_output1/processes.txt
```

The repository also includes example output in `sample_output1/` and `system_output/`.

## Commands demonstrated

`read`, variables, `mkdir`, `touch`, `echo`, `date`, `hostname`, `whoami`, `df`, `ps`, and `>` redirection.