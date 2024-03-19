#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re

def search_key_in_files(directory, search_key):
    files_containing_key = []

    # Regular expression pattern for the search key
    pattern = re.compile(search_key)

    # Traverse directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.ipynb', '.py')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    try:
                        content = f.read()
                    except UnicodeDecodeError:
                        continue
                    if re.search(pattern, content):
                        files_containing_key.append(file_path)

    return files_containing_key

# Directory to search in
directory_to_search = '/home/ubuntu/'

# Search key
# search_key = r'1ols665u6knerAyrGYzWiszWMLS__BQ1g92akcxk01DA'
search_key = r'1tj8AFk4neprEOrCI1yMtiue8bb7YMQfJcNxRM9AK4v0'

# Call the function
result = search_key_in_files(directory_to_search, search_key)

# Print the files containing the search key
if result:
    print("Files containing the search key:")
    for file in result:
        print(file)
else:
    print("No files found containing the search key.")

