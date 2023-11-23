import os

def get_files_and_folders(path):
    files_and_folders = []
    for root, directories, files in os.walk(path):
        for directory in directories:
            files_and_folders.append(os.path.join(root, directory))
        for file in files:
            files_and_folders.append(os.path.join(root, file))
    return files_and_folders

def delete_excess_files_and_folders(allowed_list, path):
    files_and_folders = get_files_and_folders(path)
    sort_files_and_folders = files_and_folders[::-1]
    for entry in sort_files_and_folders:
        if entry not in allowed_list:
            if os.path.isfile(entry):
                print('удаляю', entry)
                os.remove(entry)
            elif os.path.isdir(entry) and len(get_files_and_folders(entry))==0:
                print('удаляю директорию', entry)
                os.rmdir(entry)

def main():
    file_path = os.path.realpath(__name__)
    path = os.path.dirname(file_path)
    allowed_files_and_folders = []

    # Прочитать файл с разрешенными файлами и папками
    with open("allowed_files.txt", "r") as file:
        allowed_files_and_folders = file.read().splitlines()

    delete_excess_files_and_folders(allowed_files_and_folders, path)
    print("Операция завершена!")

if __name__ == "__main__":
    main()
