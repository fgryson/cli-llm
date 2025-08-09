import os

def get_files_info(working_directory, directory="."):
    response = ""
    directory_string = "current" if directory == "." else f"'{directory}'"
    response += f'Result for {directory_string} directory:\n'
    full_path = os.path.abspath(os.path.join(working_directory, directory))


    if not full_path.startswith(os.path.abspath(working_directory)):
        response += f'    Error: Cannot list "{directory}" as it is outside the permitted working directory\n'
        return response
    if not os.path.isdir(full_path):
        response += f'    Error: "{directory}" is not a directory\n'
        return response

    try:
        contents = os.listdir(full_path)
        for file in contents:
            file_path = os.path.join(full_path, file)
            file_size = os.path.getsize(file_path)
            is_file_dir = os.path.isdir(file_path)
            response += f' - {file}: file_size={file_size} bytes, is_dir={is_file_dir}\n'

        return response
    except Exception as err:
        response += f'    Error: {err}\n'
        return response
