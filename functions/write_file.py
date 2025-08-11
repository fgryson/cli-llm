import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        with open(full_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as err:
        return f'Error: {err}'
