import IPython

# print system information (but not packages)
print(IPython.sys_info())

# get module information
!pipreqs . --force --savepath requirements-imports.txt
!pip3 freeze > requirements-all-dependencies.txt

# append system information to file
with open("python-info.txt", "w") as file:
	file.write(IPython.sys_info())
