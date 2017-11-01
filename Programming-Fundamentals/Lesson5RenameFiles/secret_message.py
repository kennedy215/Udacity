import os

def rename_files():
    #get the file names from a folder
    file_list = os.listdir("/Users/subha/Desktop/NanoDegree-FullStackWebDevelopment/Lesson5RenameFiles/secret_message")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working directory is" +saved_path)
    os.chdir("/Users/subha/Desktop/NanoDegree-FullStackWebDevelopment/Lesson5RenameFiles/secret_message")
    #for each file, rename filename
    for file_name in file_list:
        print("Old Name -"+file_name)
        print("New Name-" +file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_files()
    
