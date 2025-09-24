import os
from google.genai import types

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        if os.path.isdir(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))
        if not abs_file_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        with open(abs_file_path, 'r') as file:
            content = file.read(MAX_CHARS)
        return content
    except Exception as e:
        return f"Error: {str(e)}"
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file, constrained to the working directory. If the file exceeds 10,000 characters, only the first 10,000 characters are returned.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
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