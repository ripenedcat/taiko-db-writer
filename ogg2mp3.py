import os
root = r'C:\Users\v-zixinh\Downloads\taiko-db-writer-master\taiko-db-writer-master'
for parent, dirnames, filenames in os.walk(root):
    for dirname in dirnames:
        pass
    for filename in filenames:
        if filename.endswith('mainmp3'):
            print("Copying", os.path.join(parent, filename), "to\n", os.path.join(parent, 'main' + ".mp3"))
            os.rename(os.path.join(parent, filename), os.path.join(parent, 'main' + ".mp3"))
