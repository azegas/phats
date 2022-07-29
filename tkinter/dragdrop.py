import sys
try:
    droppedFile = sys.argv[1] 
except IndexError:
    print("No file dropped")
