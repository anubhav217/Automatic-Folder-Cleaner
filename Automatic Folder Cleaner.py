import os

def createifNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(foldername,files):
    for file in files:
        os.replace(file,f"{foldername}/{file}")
files=os.listdir()
files.remove("main.py")
print(files)

createifNotExist('Images') #CREATES A FOLDER IMAGES
createifNotExist('Docs') #CREATES A FOLDER FOR DOCUMENTS
createifNotExist('Media') 
 #CREATES A FOLDER FOR MEDIA
createifNotExist('Others')
imgExts=[".png",".jpg",".jpeg"]
images=[file for file in files if os.path.splitext(file)[1].lower() in imgExts]
docExts=['.txt','.pdf','.docx','.pdf']
docs=[file for file in files if os.path.splitext(file)[1].lower() in docExts]
print(images)
print(docs)

mediaExts=['.mp4','.mp3','.flv']
medias=[file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
print(medias)

others=[]
for file in files:
    ext=os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)


print(others)

move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Others",others)
