import os
import shutil

def list_files(startpath, extension):
    """
    Generator to list files in directories
    """
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file.lower().endswith(extension.lower()):
                yield os.path.join(root, file)

def organize_files():
    print("Welcome to the File Organizer Tool!\n")
    print("Available Commands:")
    print("  help - Display file extension descriptions.")
    print("  enter directory - Specify the directory and file type to organize.")
    print("  move - Move files to a specified directory based on the last 'enter directory' command.")
    print("  exit - Exit the program.\n")

    disk, extension = None, None  

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
                move_files(files_to_move)
            else:
                print("No directory and file type specified, or no files to move. Please use 'enter directory' first.")
        elif command.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

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
        'csv': 'CSV file - Comma Separated Values for storing tabular data'    }
    for ext, desc in extension_descriptions.items():
        print(f".{ext} - {desc}")

def enter_directory():
    disk = input("Enter the full path of the disk or directory you want to search: ")
    extension = input("Enter the file extension you want to organize: ")
    if not extension.startswith('.'): 
        extension = '.' + extension
    return disk, extension

def move_files(files_to_move):
    destination = input("Enter the full path and folder name where you want to move the files: ")
    os.makedirs(destination, exist_ok=True)
    moved_count = 0
    for file_path in files_to_move:
        shutil.move(file_path, os.path.join(destination, os.path.basename(file_path)))
        moved_count += 1
        print(f"Moved {file_path} to {destination}")
    print(f"Total of {moved_count} files moved.")

# Start the organizer tool
organize_files()
