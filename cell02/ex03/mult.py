# -*- coding: utf-8 -*-
"""mult.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12eWW1xRv4k7wVpdgK5NWz1YVUM_yT80C
"""

f = str(input("Enter the first number:"))
s = str(input("Enter the  second number:"))
r = int(float(f)*float(s))

print(f,"x",s,"=",r)
if r > 0 :
  print("The result is positive.")
elif r < 0 :
  print("The result is negative.")
else  :
  print("The result is positive and negative.")