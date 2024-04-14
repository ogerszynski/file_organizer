import os
# dodano moduł shutil obsługujący funkcje operacji na plikach min. przenoszenie
import shutil
# dodano moduł obsługi zapisu czasu - potrzebny do zapisu do logu
import datetime

# obsługa błędów
def handle_error(error_msg):
    print(f"Error: {error_msg}")
    response = input("Do you want to continue (C) or go back (B)? ").lower()
    if response == 'c':
        return
    elif response == 'b':
        return None
    else:
        handle_error("Invalid response.")

# funkcja generowania listy plików z danym rozszerzeniem
def list_files(startpath, extension):
    """
    Generator to list files in directories
    """
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file.lower().endswith(extension.lower()):
                yield os.path.join(root, file)

# funkcja zarządzająca interakcją z userem i wykonująca operacje na plikach
def organize_files():
    print("Welcome to the File Organizer Tool!\n")
    print("Available Commands:")
    print("  help - Display file extension descriptions.")
    print("  enter directory - Specify the directory and file type to organize.")
    print("  move - Move files to a specified directory based on the last 'enter directory' command.")
    print("  exit - Exit the program.\n")

# inicjalizacja zmiennych
disk, extension, files_to_move = None, None, None  

# słownik popularnych typów rozszerzeń po wyborze polecenia help, mozna rozszerzać dowolnie o kolejne typy plików
def show_help():
    extension_descriptions = {
        'doc': 'Microsoft Word document - Text document format',
        'docx': 'Microsoft Word Open XML document - Enhanced text document format',
        'xls': 'Microsoft Excel spreadsheet - Data spreadsheet format',
        'xlsx': 'Microsoft Excel Open XML spreadsheet - Enhanced data spreadsheet format',
        'pdf': 'Portable Document Format - Reliable document file',
        'jpg': 'JPEG image - Common image format with lossy compression',
        'jpeg': 'JPEG image - Common image format with lossy compression',
        'bmp': 'Bitmap image file - Raster graphics image file format',
        'txt': 'Text file - Plain text file without special formatting',
        'ppt': 'Microsoft PowerPoint presentation - Presentation file format',
        'png': 'PNG image - Raster graphics file format that supports lossless data compression',
        'gif': 'GIF image - Bitmap image format for animated and static images',
        'mp3': 'MP3 audio file - Audio format for audio storage',
        'mp4': 'MP4 video file - Multimedia container format for video and audio',
        'csv': 'CSV file - Comma Separated Values for storing tabular data'    
    }
    for ext, desc in extension_descriptions.items():
        print(f".{ext} - {desc}")

# funkcja pobierająca ścieżkę i wracająca listę plików
def enter_directory():
    disk = input("Enter the full path of the disk or directory you want to search: ")
    extension = input("Enter the file extension you want to organize: ")
    if not extension.startswith('.'): 
        extension = '.' + extension
    return disk, extension

# funkcja przenoszenia plików
def move_files(destination, files_to_move):
    if not check_disk_space(destination, files_to_move):  # sprawdzenie dostępnego miejsca
        handle_error("Not enough space on the destination disk.")
        return
    os.makedirs(destination, exist_ok=True)
    moved_count = 0
    failed_files = []  
    moved_files = []  
    for file_path in files_to_move:
        try:
            shutil.move(file_path, os.path.join(destination, os.path.basename(file_path)))
            moved_count += 1
            moved_files.append(file_path)  # 
            print(f"Moved {file_path} to {destination}")
        except Exception as e:
            print(f"Failed to move {file_path}: {e}")
            failed_files.append(file_path)  #

    # funkcja zapisu do logu
    def write_to_log(files_moved):
        log_file = "file_organizer_log.txt"
        with open(log_file, 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Files moved on {timestamp}:\n")
            for file_path in files_moved:
                f.write(f"{file_path}\n")
            f.write("\n")
        print(f"Log file '{log_file}' updated with the list of moved files.")

    def write_to_log_failed(failed_files):
        log_file = "file_organizer_errors.txt"
        with open(log_file, 'a') as f:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"Errors occurred on {timestamp}:\n")
            for file_path in failed_files:
                f.write(f"{file_path}\n")
            f.write("\n")
        print(f"Error log file '{log_file}' updated with the list of failed files.")

    #wywałanie funkcji zapisu do logu
    write_to_log(moved_files)
    write_to_log_failed(failed_files)

# sprawdzenie miejsca w folderze docelowym
def check_disk_space(destination, files_to_move):
    total_size = sum(os.path.getsize(file_path) for file_path in files_to_move)
    free_space = shutil.disk_usage(destination).free
    if total_size > free_space:
        return False
    return True

# główna pętla
while True:
    command = input("Enter a command (help, enter directory, move, exit): ")

    if command.lower() == 'help':
        show_help()
    elif command.lower() == 'enter directory':
        disk, extension = enter_directory()
        files_to_move = list(list_files(disk, extension))
        if files_to_move:
            print("Files found:")
            for f in files_to_move:
                print(f)
        else:
            print(f"No files with the {extension} extension found in {disk}.")
    elif command.lower() == 'move':
        if disk and extension and files_to_move:
            destination = input("Enter the full path and folder name where you want to move the files: ")
            move_files(destination, files_to_move)
        else:
            print("No directory and file type specified, or no files to move. Please use 'enter directory' first.")
    elif command.lower() == 'exit':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")

# Start the organizer tool
organize_files()
