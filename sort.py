import os
import time


os.system('cls')



values = [10, 4, 3, 2, 5, 1, 6, 8, 9, 7]


print("Your list:", values)

print("\n\nSorting...\n")

for all in values:
   for i in range(len(values)):
      temp = values[i]
   
      if i+1 < len(values):
         if values[i+1] < values[i]: #is the proceeding number smaller? theen switch it up
            values[i] = values[i+1]  # switch positions
            values[i+1] = temp       # switch positions

time.sleep(0.65)
print("Sorted:", values)