# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints
# 1<=n<=100
# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0
# n=33
# nis odd and odd numbers are weird, so print Weird

Logic 2

import math
import os
import random
import re
import sys


n=int(input().strip());
if(n%2==0 and 2>=n<=5):
    Print("Not Weird");
elif(n%2==0 and 6>=n<=20):
    print("Weird");
elif(n%2==0 and n>20):
    print("Not Weird");
elif(n%2!=0):
    print("Weird");
else:
    print("check the number");


