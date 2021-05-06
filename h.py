import os

import shutil
import time




def GetNameOfFile(i):
    return "file_" + str(i) + ".syamich"



def WriteStorage(name_of_disk):
    """ Setting variables """
    temp_folder = 'temp'
    path = name_of_disk.upper() + ':\\'


    os.chdir(path) # Changing path to the disc that must be cleaned
    random_bytes = os.urandom(5000000) # Write 5000000 random bytes = 14MB


    # print(shutil.disk_usage(name_of_disk.upper() + ':\\'))

    # Creating temp derictory
    os.system("mkdir " + temp_folder)
    print('Temp folder created')

    # Open temp directory
    os.chdir(temp_folder)




    i = 1
    a = False
    free = shutil.disk_usage(path).free
    os.system("NUL> " + GetNameOfFile(i))
    f = open(GetNameOfFile(i), "w")
    f.write(''+str(random_bytes))
    start_time = time.time()
    stop_time = 0
    start_storage = shutil.disk_usage(path).free

    print('Procces started')

    try:
        while free > 15000000:
            i += 1
            src = GetNameOfFile(1)
            dst = GetNameOfFile(i)
            shutil.copyfile(src, dst, follow_symlinks=True)
            free = shutil.disk_usage(path).free
            if (i == 100):
                a = True
                stop_time = time.time()
            if a:
                a = False
                total = shutil.disk_usage(path).total
                x = free / (start_storage - free)
                print(str((stop_time - start_time) * x) + ' seconds left')
                print('Speed: ' + str( ((start_storage - free) / (stop_time - start_time)) / (1024 * 1024) ) + ' MB/s')
    except Exception as e:
        print(e)

    i = 1

    free = shutil.disk_usage(path).free
    os.system("NUL> " + GetNameOfFile(i) + 'byte')
    f = open(GetNameOfFile(i) + 'byte', "w")
    f.write(str(os.urandom(10)))
    try:
        while free > 100:
            i += 1
            src = GetNameOfFile(1) + 'byte'
            dst = GetNameOfFile(i) + 'byte'
            shutil.copyfile(src, dst, follow_symlinks=True)
            free = shutil.disk_usage(path).free
    except Exception as e:
        print(e)

    # Removing the files
    f.close()

    os.chdir(path)
    os.system("rd /s /q " + temp_folder)
    print('папка удалена')

    # print(os.getcwd()) # Get current directory




def main():
	print('Enter disk letter: ')
	l = input()
	WriteStorage(l)

if __name__ == "__main__":
	main()
