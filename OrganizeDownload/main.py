import os

file_path = 'C:/Users/egoit/Downloads/folder_to_be_deleted'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print('File successfully removed!')
else:
    print('This file does NOT exist')