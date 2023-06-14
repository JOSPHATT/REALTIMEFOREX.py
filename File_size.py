# approach 1
# using getsize function os.path module
import os
import time
T=time.asctime()
Size={}
file_size = os.path.getsize('realtimeforex.txt')
Size[T]=file_size
print(Size)
