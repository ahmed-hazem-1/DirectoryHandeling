import os
import shutil

current_path = os.getcwd()

for file in os.listdir(current_path):

    ## Set the Expectation for the HandelDirectort.py
    if file == "HandelDirectory.py":
        continue

    ## Handel the imgs to Images folder
    if file.endswith(("png", "jpeg", "jpg", "gif")):
        if not os.path.exists("Images"):
            os.mkdir("Images")
        shutil.move(file, "Images")
        print(f"Moved {file} to Images folder")

    ## Handel the Docs and PDFs to Documentations folder
    if file.endswith(('pdf', 'docx', 'doc', 'ppt', 'pptx', 'xlsx', 'xls', 'txt')):
        if not os.path.exists("Documentations"):
            os.mkdir("Documentations")
        shutil.move(file, "Documentations")
        print(f"Moved {file} to Documentations folder")

    ## Handel the Videos to Videos folder
    if file.endswith(('mp4', 'mkv', 'avi', 'flv', 'mov')):
        if not os.path.exists("Videos"):
            os.mkdir("Videos")
        shutil.move(file, "Videos")
        print(f"Moved {file} to Videos folder")

    ## Handel the Audios to Audios folder
    if file.endswith(('mp3', 'wav', 'ogg', 'flac')):
        if not os.path.exists("Audios"):
            os.mkdir("Audios")
        shutil.move(file, "Audios")
        print(f"Moved {file} to Audios folder")

    ## Handel the Zips to Compressed folder
    if file.endswith(('zip', 'rar', '7z', 'tar')):
        if not os.path.exists("Compressed"):
            os.mkdir("Compressed")
        shutil.move(file, "Compressed")
        print(f"Moved {file} to Compressed folder")

    ## Handel the Exes to Applicatons folder
    if file.endswith(('exe', 'msi')):
        if not os.path.exists("Applications"):
            os.mkdir("Applications")
        shutil.move(file, "Applications")
        print(f"Moved {file} to Applications folder")

    ## Handel the Scripts to Scripts folder
    if file.endswith(('py', 'sh', 'bat')):
        if not os.path.exists("Scripts"):
            os.mkdir("Scripts")
        shutil.move(file, "Scripts")
        print(f"Moved {file} to Scripts folder")
