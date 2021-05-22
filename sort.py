import os
from shutil import copyfile

dir_id=1

FILE_LOCATIONS = ['fumen/JPOP/', 'fumen/Anime/', 'fumen/Classic/', 'fumen/Game/', 'fumen/Kid/', 'fumen/Namco/', 'fumen/Varity/', 'fumen/Vocaloid/', 'fumen/Others/']

for catagory_dir in FILE_LOCATIONS:
    # for parent, dirnames, filenames in os.walk(catagory_dir):
    #     for dirname in dirnames:
    #         pass
    #     for filename in filenames:
    #         if filename.endswith('.ogg') or filename.endswith('tja'):
    #             suffix = os.path.splitext(os.path.join(parent,filename))[-1]
    #             print("Copying",os.path.join(parent,filename),"to\n",os.path.join(parent,'main'+suffix))
    #             os.rename(os.path.join(parent,filename),os.path.join(parent,'main'+suffix))


                #print(os.path.join(parent,filename))
                #suffix = os.path.splitext(os.path.join(parent,filename))[-1]
                #copyfile(os.path.join(parent,filename),os.path.join(result_path, str(dir_id),'main'+suffix))
    for parent, dirnames, filenames in os.walk(catagory_dir):
        for dirname in dirnames:
            os.rename(os.path.join(parent,dirname),os.path.join(parent,str(dir_id)))
            dir_id += 1
print('done')