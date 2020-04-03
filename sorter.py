import os
import shutil
import json

'''Originally posted on: github.com/1a11/sortify'''


print('Reading config.json...')
try:
    with open("config.json", "r") as read_file:
        data = json.load(read_file)
except Exception:
    print("Can't find config.json")
else:
    print('Reading file-tree...')
    
    

    for i in data:
        try:
            os.mkdir(i)
        except Exception:
            pass
        
    print('Sorting...\n\n')
    for file in files:
        if '.' in i:
            ex = file.split('.')
            moved = False
            for extype in data:
                if ex[len(ex)-1] in data[extype] and not moved:
                    print('{} moved to {}'.format(file, data[extype]))
                    try:
                        shutil.move('./'+file, './'+extype)
                        moved = True
                    except Exception:
                        pass
            if not moved:
                print('{} moved to Other'.format(file))
                try:
                    shutil.move('./'+file, './Other')
                except Exception:
                    pass
        else:
            print('{} moved to Folders'.format(i))
            try:
                shutil.move('./'+file, './Folders')
            except Exception:
                pass
    print('\n\nDone.')
