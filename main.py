import os
import sys
from dotenv import load_dotenv
from google.genai import types, Client
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = Client(api_key=api_key)

system_prompt =system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

When the user asks about the code project - they are referring to the working directory. So, you should typically start by looking at the project files, figuring out how to run the project files and tests. You'll always want to run the tests and the actual project to verify that the behaviour is working.

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

if len(sys.argv) < 2:
    print("Usage: python main.py '<your prompt here>'")
    sys.exit(1)
verbose = sys.argv[2] if len(sys.argv) > 2 else "false"
prompt = sys.argv[1]

messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

res = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        tools=[available_functions]
    )
    )

if res.candidates:
    for candidate in res.candidates:
        messages.append(candidate.content)

if res.function_calls:
    for fc in res.function_calls:
        try:
            function_call_result = call_function(fc, verbose)
            
            print(function_call_result)
        except Exception as e:
            print(f"Error: {e}")
else:
    print(res.text)

if verbose.lower() == "--verbose":
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {res.usage_metadata.candidates_token_count}")