import os
import shutil
import glob
import time

while(1 == 1):
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    files = glob.glob(os.path.join(downloads_path, '*'))
    files.sort(key=os.path.getmtime, reverse=True)
    for i in range(len(files)):
        if ".zip" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/Zipfiles")
        elif ".7z" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/Zipfiles")
        elif ".rar" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/Zipfiles")
        elif".pdf" in files[i]:
            shutil.move(files[i],"C:/Users/sansh/Downloads/pdfs")
        elif ".jpeg" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/images")
        elif ".jpg" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/images")
        elif ".png" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/images")
        elif ".avif" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/images")
        elif ".gif" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/images")
        elif ".mp4" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/videos")
        elif ".py" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/python_files")
        elif ".csv" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/csv")
        elif ".ico" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/icons")
        elif ".mp3" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/music")
        elif "april" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/Youtube")
        elif ".exe" in files[i]:
            shutil.move(files[i], "C:/Users/sansh/Downloads/application")
        elif ".tmp" in files[i]:
            time.sleep(20)
        elif shutil.Error:
            continue



















