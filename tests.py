from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

print("lorem.txt file content:")
result=get_file_content("calculator","lorem.txt")
print(result)

print("main.py file content:")
result=get_file_content("calculator","main.py")
print(result)

print("calculator.py ffile content:")
result=get_file_content("calculator","pkg/calculator.py")
print(result)

print("bin cat file content:")
result=get_file_content("calculator","/bin/cat")
print(result)

print("does not exist file content: ")
result=get_file_content("calculator","pkg/does_not_exist.txt")
print(result)
