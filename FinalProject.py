import os
import shutil
from hashlib import md5
from numpy.random import randint
from send2trash import send2trash
from collections import defaultdict

documentsfile = r"C:\Users\HP\Documents"
videosfile = r"C:\Users\HP\Videos"
picturesfile = r"C:\Users\HP\OneDrive\الصور"
musicfile = r"C:\Users\HP\Music"

EXTDEST = {
        ".exe": documentsfile,
        ".msi": documentsfile,
        ".vtt": documentsfile,
        ".srt": documentsfile,
        ".pdf": documentsfile,
        ".pptx": documentsfile,
        ".docx": documentsfile,
        ".accdb": documentsfile,
        ".pub": documentsfile,
        ".csv": documentsfile,
        ".xlsx": documentsfile,
        ".html": documentsfile,
        ".sql": documentsfile,
        ".psd": documentsfile,
        ".aep": documentsfile,
        ".ai": documentsfile,
        ".mov": videosfile,
        ".mp4": videosfile,
        ".avi": videosfile,
        ".png": picturesfile,
        ".jpg": picturesfile,
        ".jpeg": picturesfile,
        ".gif": picturesfile,
        ".mp3":musicfile,
        ".wav":musicfile,
        ".zip":"extract",
        ".tar":"extract",
        ".gz":"extract",
        ".xz":"extract",
        ".bz2":"extract"
    }

def all_directories(maindir: str) -> list:
  directories = []
  for root, dirs, _ in os.walk(maindir):
    for dir in dirs:
      dir = os.path.join(root, dir)
      directories.append(dir)
    break
  return directories

def all_files(directory: str) -> list:
  Files = []
  for root , _ , files in os.walk(directory):
    for f in files:
      f = os.path.join(root , f)
      Files.append(f)
    break
  return Files

def find_duplicate_files(directory: str, hash_size: int = 1024*512) -> None: # 1024 chunk = 1kb
  print("Searching for duplicate files...")

  files = all_files(directory)

  file_hashes = defaultdict(list)

  for file in files:
    file_hash = hash_file(file, hash_size)
    file_hashes[file_hash].append(file)
  
  for file_hash, file_list in file_hashes.items():
    if len(file_list) > 1:
      print(f"\nDuplicate files found (hash: {file_hash}):")
      for i, file_path in enumerate(file_list, 1):
        print(f"{i}. {file_path}")
    
      print(f"FILE: {file_list[-1]} REMOVED.")
      send2trash(file_list[-1])
        
def hash_file(filepath: str, hash_size: int, block_size: int = 8192): # 8192 chunk = 8kb
  hasher = md5()
  with open(filepath, 'rb') as file:
    size_read = 0
    while size_read < hash_size:
      chunks = file.read(block_size)
      if not chunks:
        break
      hasher.update(chunks)
      size_read += len(chunks)
  return hasher.hexdigest()

def find_duplicate_folders(directory: str) -> None:
  print("Searching for duplicate folders...")

  all_dirs = all_directories(directory)

  dir_groups = defaultdict(list)

  for current_dir in all_dirs:
    dir_key = generate_key(current_dir)
    dir_groups[dir_key].append(current_dir)
  
  for key, directories in dir_groups.items():
    if len(directories) > 1:
      print("\nPotential duplicates found:")
      for D in directories:
        print(f"- {D}")
      
      send2trash(directories[-1])
      
def generate_key(directory: str) -> str:
  key_parts = []
  for root, dirs, files in os.walk(directory):
    relpath = os.path.relpath(root, directory)
    key_parts.append(f"DIR:{relpath}")
    for file in files:
      file_path = os.path.join(root, file)
      rel_file_path = os.path.relpath(file_path, directory)
      file_size = os.path.getsize(file_path)
      key_parts.append(f"FILE:{rel_file_path}:{file_size}")
  
  return ";".join(key_parts)

def extract_files(maindir: str) -> None:
  extracted_files_count = 0
  for root, _, files in os.walk(maindir):
    for file in files:
      file_path = os.path.join(root, file)
      extension = os.path.splitext(file_path)[1].lower()
      if EXTDEST.get(extension) == "extract":
        try:
          unpacked_path = os.path.splitext(file_path)[0]
          shutil.unpack_archive(file_path, unpacked_path)
          send2trash(file_path)
          print(f"File {file_path} unpacked to {unpacked_path}")
          extracted_files_count += 1
        except Exception as e:
          print(f"Error extracting {file_path}: {str(e)}")
    break
  if extracted_files_count > 0:
    print(f"Extracting process finished. {extracted_files_count} file(s) extracted.\n")
  else:
    print("No files were extracted.\n")

def rename_file(pathName:str) -> str:
  new_name = pathName + str(randint(0,10))
  return new_name
  
def create_dir(path: str, extension: str) -> str:
  new_folder = os.path.join(path, extension)
  if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print(f"New directory is created: {new_folder}")
    return new_folder
  else:
    anotherName = rename_file(new_folder)
    os.mkdir(anotherName)
    print(f"New directory is created: {anotherName}")
    return anotherName

def FinalDestination(destination: str, extension: str) -> str:
  result = _find_final_destination(destination, extension)
  if result:
    return result
  else:
    return create_dir(destination, extension.removeprefix('.'))

def _find_final_destination(destination: str, extension: str) -> str:
  with os.scandir(destination) as dir:
    sorted_dir = sorted(dir, key=lambda entry: (entry.is_dir(), entry.name))

    for entry in sorted_dir:

      if entry.is_dir() and not entry.is_junction():
        path = _find_final_destination(entry.path, extension)
        if path:
          return path

      elif entry.is_file() and entry.name.endswith(extension):
        return entry.path.removesuffix("\\" + entry.name)

def move_file(source: str, destination: str) -> None:
  filename = os.path.basename(source)
  duplicate_check = os.path.join(destination , filename)
  if os.path.exists(duplicate_check):
    file_size1 = os.stat(source).st_size
    file_size2 = os.stat(duplicate_check).st_size
    if file_size1 == file_size2:
      send2trash(duplicate_check)
      print(f"Duplicate Found! {filename} In {destination} Sent To Recycle Bin")
    else:
      new_file_name = rename_file(os.path.splitext(source)[0])
      os.rename(source , new_file_name)
      print(f"Similar Names Detected! {os.path.basename(source)} Changed To {os.path.basename(new_file_name)}")

  if os.path.exists(source):
    shutil.move(source, destination)
    print(f"File Moved From {source} To {destination}")
  elif os.path.exists(new_file_name):
    shutil.move(new_file_name, destination)
    print(f"File Moved From {new_file_name} To {destination}")

def Modify(maindir: str) -> None:
  if not any(os.scandir(maindir)):
    print("انت تسوق امها")
    return
  
  _process_root(maindir)

def _process_root(maindir: str) -> None:
  with os.scandir(maindir) as dir:
    sorted_dir = sorted(dir, key=lambda entry: (entry.is_dir(), entry.name))
    for entry in sorted_dir:

      if entry.is_dir():
        dir_ext = _process_subdirectories(entry.path)
        if dir_ext:
          handle_item(entry.path, dir_ext)
        
      elif entry.is_file() and entry.name != "desktop.ini":
        handle_item(entry.path)

def _process_subdirectories(directory: str) -> str:
  with os.scandir(directory) as subdir_entries:
    sorted_entries = sorted(subdir_entries, key=lambda entry: (entry.is_dir(), entry.name))
    for entry in sorted_entries:

      if entry.is_dir() and not entry.is_junction():
        ext = _process_subdirectories(entry.path)
        if ext:
          return ext
        
      elif entry.is_file() and entry.name != 'desktop.ini':
        return os.path.splitext(entry.name)[1]
  
  send2trash(directory)
  print(f"Directory {directory} Sent To Recycle Bin!")
  return
  
def handle_item(path: str, dir_ext = None) -> None:
  EXT = dir_ext if dir_ext else os.path.splitext(path)[1]
  destination = EXTDEST.get(EXT)
  
  try:
    final_destination = FinalDestination(destination, EXT)
    move_file(path, final_destination)
  except TypeError:
    print("Extension Is Not Supported.")

if __name__ == "__main__":
  extract_files(r"C:\Users\HP\Desktop\Main Directory")
  find_duplicate_folders(r"C:\Users\HP\Desktop\Main Directory")
  find_duplicate_files(r"C:\Users\HP\Desktop\Main Directory")
  Modify(r"C:\Users\HP\Desktop\Main Directory")

