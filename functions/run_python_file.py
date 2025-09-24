import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            f'Error: "{file_path}" is not a Python file.'
        output = subprocess.run(
            ['python3',abs_file_path],
            cwd =abs_working_directory,
            capture_output=True,
            timeout=30,
        )
        final_output=f"STDOUT: {output.stdout.decode()} STDERR: {output.stderr.decode()}"
        if output.returncode != 0:
            final_output += f"Error: Process exited with code {output.returncode}"
        return final_output.strip() if final_output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {str(e)}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file with optional arguments, constrained to the working directory. Captures and returns the standard output and error output of the execution.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Additional parameters to pass to the function",
                items=types.Schema(
                    type=types.Type.STRING,
                )
            ),
        },
    ),
)
