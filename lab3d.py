#!/usr/bin/env python3
import subprocess

p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

#output = p.communicate()
#stdout = output[0].decode('utf-8').strip()
#print(stdout)

def free_space():
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

print(free_space())