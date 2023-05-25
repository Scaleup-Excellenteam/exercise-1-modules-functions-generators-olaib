import os

FILE_DIDNT_EXIST_MSG = "The path does not exist or is not a folder"


def is_exist_dir(folder):
    """
    :param folder: path to the folder
    :return: True if the folder exists and is a folder
    """
    return os.path.exists(folder) and os.path.isdir(folder)


def get_files_list(folder_path: str) -> list:
    """
    :param folder_path: path to the folder
    :return: list of files in the folder that start with "deep"
    """
    # Get list of folders in the directory
    list_dir = os.listdir(folder_path)
    # Filter the list of files to get only the files that start with "deep"
    filtered_list = [file for file in list_dir if
                     file.startswith("deep") and os.path.isfile(os.path.join(folder_path, file))]
    return filtered_list


# ================== MAIN ==================
if __name__ == "__main__":
    path = input("Enter the file path: ")
    assert is_exist_dir(path), FILE_DIDNT_EXIST_MSG
    files = get_files_list(path)
    print("Files in the folder that start with 'deep':")
    print('\n'.join([f"{i + 1}. {file}" for i, file in enumerate(files)]))
