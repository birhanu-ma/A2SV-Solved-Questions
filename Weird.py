#!/bin/python3

import math
import os
import random
import re
import sys

def Weird(num):
    if num%2 != 0:
        print("Weird")
    elif num%2 == 0 and 2<= num <= 5:
        print("Not Weird") 
    elif num%2 == 0 and 6<= num <= 20:
        print("Weird")     
    elif num%2 == 0 and num > 20:
        print("Not Weird")    
if __name__ == '__main__':
    n = int(input().strip())
    Weird(n)
