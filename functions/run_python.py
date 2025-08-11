import os, subprocess, sys

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found...'
        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        try:
            command = ['python', full_path]
            if args:
                command.extend(args)

            completed_process = subprocess.run(
                command,
                cwd=working_directory,
                timeout=30,
                capture_output=True,
                text=True
            )
            
            stdout = completed_process.stdout.strip()
            stderr = completed_process.stderr.strip()
            return_code = completed_process.returncode

            output = []
            if stdout:
                output.append(f'STDOUT: {stdout}')
            if stdout:
                output.append(f'STDERR: {stderr}')
            if return_code != 0:
                output.append(f'Process exited with code {return_code}')
            
            if not output:
                return "No output produced."
            else:
                return "\n".join(output)

        except Exception as err:
            return f'Error: executing Python file: {err}'

    except Exception as err:
        return f'Error: {err}'
