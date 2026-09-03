#!/bin/bash

current_date=$(date)
hostname=$(hostname)
username=$(whoami)

# Take user input
read -p "Enter a directory name: " directory

# Create directory
mkdir -p "$directory"

# Create a file inside the directory
touch "$directory/processes.txt"

# Display system information
echo "===== SYSTEM INFORMATION ====="
echo "Date: $current_date"
echo "Hostname: $hostname"
echo "Username: $username"

echo ""
echo "===== DISK USAGE ====="
df -h

echo ""
echo "===== RUNNING PROCESSES ====="
ps

# Store running processes in the file
ps > "$directory/processes.txt"

echo ""
echo "Running processes have been saved to $directory/processes.txt"