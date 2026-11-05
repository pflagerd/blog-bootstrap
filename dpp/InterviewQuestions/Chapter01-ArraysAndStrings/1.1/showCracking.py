#!/usr/bin/python
import subprocess

subprocess.Popen(["okular", "../../../../Cracking the Coding Interview 189 Programming Questions and Solutions.pdf", "-p", "101", "--find", "1.1"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.Popen(["okular", "../../../../Cracking the Coding Interview 189 Programming Questions and Solutions.pdf", "-p", "664"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
