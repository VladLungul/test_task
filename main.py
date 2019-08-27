import os
import time
from config import file_path, Handler

files = os.listdir(file_path)

def difference_list(x, y):
    difference = []
    for i in x:
        if i not in y:
            difference.append(i)
    for j in y:
        if j not in x:
            difference.append(j)
    return difference

while True:
    new_files = os.listdir(file_path)
    d = difference_list(files, new_files)

    if not d:
        pass
    else:
        a = Handler.choose_handler(d)

    files = new_files
    time.sleep(0.5)









