import os, shutil

# CHANGE THE PATH TO THE DESIRED DIRECTORY
path = r"C:\Users\username\Downloads"

# LISTING ALL FILES IN DIRECTORY
files = [f for f in os.listdir(path) if os.path.isfile(path+rf"\{f}")]

# LIST OF ALL FOLDERS FOR STORING FILES
folders = ["applications", "audio", "zip files", "images", "docs", "videos", "presentations", "webpages", "codes"]

# EXTENSIONS POINTING TO RESPECTIVE DIRECTORY
directories = {

    ".html5.html.htm.xhtml.aspx.php.webp": "webpages",

    ".jpg.jpeg.png.tiff.gif.bmp.bpg.svg.heif.psd.jfif": "images" ,

    ".avi.mp4.flv.mkv.wmv.mov.webm.vob.3gp.mpeg.mpg.qt": "videos",

    ".pdf.doc.docx.xls.xlsx.ppt.pptx.epub.opus.txt.in.out.xml": "docs",

    ".rar.zip.7z": "zip files" ,

    ".mp3.aac.ogg.m4a.wav.aa.dvf.m4b.m4p.msv.oga.raw.vox": "audio" ,

     ".exe.apk.msi":"applications",

     ".py.cpp.c++.cp.js.jsp.ipynb.java": "codes"

}

existing_dir = [d for d in os.listdir(path) if os.path.isdir(path+rf"\{d}")]
# CREATING NEW DIRECTORIES IF NOT ALREADY PRESENT
for dir in folders:
    if dir in existing_dir:
        continue
    os.mkdir(path + rf"\{dir}")

# MOVING FILES TO RESPECTIVE DIRECTORIES
for x in files:
     suffix = x.split(".")[-1]
     f_path = path + rf"\{x}"
     for key in directories.keys():
          if suffix in key:
               try:
                    shutil.move(f_path, path+rf"\{directories[key]}")
               # IN CASE OF ANY EXCEPTIONS IGNORE CURRENT FILE 
               # (usually occurs when file is already present in the directory)
               except Exception as e:
                    print(f"Failed to move {x} : {e}")
