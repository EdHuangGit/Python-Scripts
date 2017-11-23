import os

#check for root privileges
if os.geteuid() != 0:
    exit("You need to have root privileges to run this script")

#set the file paths
environment = os.path.join("/etc", "environment")

def toggle_comment(line):
    if line.startswith('#'):
	return line[1:]
    else: 
	return '#' + line

lines = list()

#Remove/add proxy to the both the files
with open(environment, "r") as f:
    for line in f:
        if 'proxy' in line.lower():
	    lines.append(toggle_comment(line))
	else:
	    lines.append(line)
with open(environment, "w") as f:
   for line in lines:
        f.write(line)
