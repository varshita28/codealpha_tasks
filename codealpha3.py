import os
import shutil

file_types = {
    'TextFiles': ['.txt', '.doc', '.docx', '.pdf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Spreadsheets': ['.xls', '.xlsx', '.csv'],
    'Presentations': ['.ppt', '.pptx']
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    os.chdir(directory)
    for folder in file_types.keys():
        if not os.path.exists(folder):
            os.makedirs(folder)
    for file_name in os.listdir(directory):
        if os.path.isdir(file_name):
            continue
        _, file_extension = os.path.splitext(file_name)
        moved = False
        for folder, extensions in file_types.items():
            if file_extension.lower() in extensions:
                shutil.move(file_name, os.path.join(folder, file_name))
                moved = True
                break
        if not moved:
            if not os.path.exists('Others'):
                os.makedirs('Others')
            shutil.move(file_name, os.path.join('Others', file_name))

    print(f'Files in {directory} have been organized.')

if __name__ == '__main__':
    target_directory = '/Users/varshininaravula/Downloads'  
    organize_files(target_directory)

