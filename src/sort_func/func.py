import os
import shutil
from pathlib import Path
from transliterate import translit
import re

path = "C:\\Users\\misha\\PycharmProjects\\goit.6\\ELEMENTS"
os.listdir(path)

extensions_met = []
extensions_not_met = []
catalog = []

path_images = path + "\\images"
path_documents = path + "\\documents"
path_audio = path + "\\audio"
path_video = path + "\\video"
path_archives = path + "\\archives"


try:
   os.mkdir(path_images)
except:
   pass
try:
   os.mkdir(path_documents)
except:
   pass
try:
   os.mkdir(path_audio)
except:
   pass
try:
   os.mkdir(path_video)
except:
   pass
try:
   os.mkdir(path_archives)
except:
   pass


def normal(letter):
   changed = ''
   for j in letter:
      if bool(re.search('[а-яА-Я]', j)) == True:
         z = translit(j, language_code='ru', reversed=True)
         changed = changed + z
      elif bool(re.search('[A-Za-z0-9.]', j)) == True:
         changed = changed + j
      else:
         changed = changed + "_"
   return changed


def house_to_house_searches(path):
   for d in os.listdir(path):
      a = os.path.join(path, d)
      if os.path.isdir(a):
         house_to_house_searches(a)
         if not os.listdir(a):
            if os.path.basename(a) == "images" or os.path.basename(a) == "documents" or os.path.basename(a) == "audio" or os.path.basename(a) == "video" or os.path.basename(a) == "archives":
               pass
            else:
               os.rmdir(a)


def func(old_path, path, level = 1):
   for i in os.listdir(path):
      new_word = normal(os.path.basename(i))
      if os.path.basename(path + '\\' + i) != new_word:
         os.rename(path + '\\' + i, path + "\\" + new_word)
         i = new_word
      if os.path.isdir(path + '\\' + i):
         if os.path.basename(path + '\\' + i) == "images" or os.path.basename(path + '\\' + i) == "documents" or os.path.basename(path + '\\' + i) == "audio" or os.path.basename(path + '\\' + i) == "video" or os.path.basename(path + '\\' + i) == "archives":
            pass
         else:
            func(path, path + '\\' + i,level+1)
      else :
         if Path(path + '\\' + i).suffix == '.jpeg' or Path(path + '\\' + i).suffix == '.png' or Path(path + '\\' + i).suffix == '.jpg' or Path(path + '\\' + i).suffix == '.svg':
            extensions_met.append(Path(path + '\\' + i).suffix)
            catalog.append(os.path.basename(path + '\\' + i))
            try:
               shutil.move(path + '\\' + i, path_images)
            except:
               pass
         elif Path(path + '\\' + i).suffix == '.avi' or Path(path + '\\' + i).suffix == '.mp4' or Path(path + '\\' + i).suffix == '.mov' or Path(path + '\\' + i).suffix == '.mkv':
            extensions_met.append(Path(path + '\\' + i).suffix)
            catalog.append(os.path.basename(path + '\\' + i))
            try:
               shutil.move(path + '\\' + i, path_video)
            except:
               pass
         elif Path(path + '\\' + i).suffix == '.doc' or Path(path + '\\' + i).suffix == '.docx' or Path(path + '\\' + i).suffix == '.pdf' or Path(path + '\\' + i).suffix == '.txt' or Path(path + '\\' + i).suffix == '.xlsx' or Path(path + '\\' + i).suffix == '.pptx':
            extensions_met.append(Path(path + '\\' + i).suffix)
            catalog.append(os.path.basename(path + '\\' + i))
            try:
               shutil.move(path + '\\' + i, path_documents)
            except:
               pass
         elif Path(path + '\\' + i).suffix == '.mp3' or Path(path + '\\' + i).suffix == '.ogg' or Path(path + '\\' + i).suffix == '.wav' or Path(path + '\\' + i).suffix == '.amr':
            extensions_met.append(Path(path + '\\' + i).suffix)
            catalog.append(os.path.basename(path + '\\' + i))
            try:
               shutil.move(path + '\\' + i, path_audio)
            except:
               pass
         elif Path(path + '\\' + i).suffix == '.zip' or Path(path + '\\' + i).suffix == '.gz' or Path(path + '\\' + i).suffix == '.tar':
            shutil.unpack_archive(path + '\\' + i, path_archives)
            extensions_met.append(Path(path + '\\' + i).suffix)
            catalog.append(os.path.basename(path + '\\' + i))
            try:
               shutil.move(path + '\\' + i, path_archives)
            except:
               pass
         else:
            extensions_not_met.append(Path(path + '\\' + i).suffix)

def sorted(path):
   func(path, path)
   print("Extensions changed : ")
   print(extensions_met)
   print("Extensions not changed : ")
   print(extensions_not_met)
   print("Catalog")
   print(catalog)
   house_to_house_searches(path)


























