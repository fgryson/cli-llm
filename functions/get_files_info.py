import os

def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, directory))

        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        return "\n".join(map(file_summary(full_path), os.listdir(full_path)))
    except Exception as err:
        return f'Error: {err}'

def file_summary(full_path):
    def summarizer(file):
        file_path = os.path.join(full_path, file)
        file_size = os.path.getsize(file_path)
        is_file_dir = os.path.isdir(file_path)
        return f' - {file}: file_size={file_size} bytes, is_dir={is_file_dir}'

    return summarizer
    
