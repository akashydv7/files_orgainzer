import os, shutil

#change the path to desired directory
path = r"C:\Users\username\Downloads"

files = [f for f in os.listdir(path)]

folders = ["applications", "music", "zip files", "images", "docs", "videos", "presentations"]

for dir in folders:
    if dir in files:
        continue
    os.mkdir(path + rf"\{dir}")

apps = path + r"\applications"
music = path + r"\music"
presentations = path + r"\presentations"
zips = path + r"\zip files"
images = path + r"\images"
docs = path + r"\docs"
vids = path +r"\videos"

#sorting files on the basis of their extension

for x in files:
     f_path = path + rf"\{x}"
     if x.endswith(".mp3"):
          shutil.move(f_path, music)

     elif x.endswith(".exe"):
          shutil.move(f_path, apps)

     elif x.endswith(".pdf") or x.endswith(".docx") or x.endswith(".xlsx") or x.endswith("txt"):
          shutil.move(f_path, docs)

     elif x.endswith(".rar") or x.endswith(".zip"):
          shutil.move(f_path, zips)

     elif x.endswith(".pptx"):
          shutil.move(f_path, presentations)

     elif x.endswith(".png") or x.endswith(".jpg")or x.endswith(".jpeg"):
          shutil.move(f_path, images)

     elif x.endswith(".mp4") or x.endswith(".mkv"):
          shutil.move(f_path, vids)
