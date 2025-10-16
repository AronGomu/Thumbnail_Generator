import os

def ensure_directory_exists_for_file(filepath):
    directory = os.path.dirname(filepath)

    if directory and not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory)
    elif not directory:
        pass
    else:
        pass