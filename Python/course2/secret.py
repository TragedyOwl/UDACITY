import os

def rename_file():
    files = os.listdir(r"D:\develop\workspace\my\python\Udacity\Python\course2\data\prank")
    print(files)

    os.chdir(r"D:\develop\workspace\my\python\Udacity\Python\course2\data\prank")

    for file in files:
        os.rename(file, file.translate(str.maketrans('','','1234567890')))


rename_file()


