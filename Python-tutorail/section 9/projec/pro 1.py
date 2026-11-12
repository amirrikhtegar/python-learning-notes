import os

# * 1

# def input_cr():
#     while True:    
#         x = input("you can Write in file!:''")
#         if x != "exit":
#             with open("output.txt", "a", encoding="utf-8") as file:
#                 file.write(f"{x}\n")
#         else:
#             print("end of time you can write in file")
#             break


# input_cr()

# * 2

# with open("file_to_delete.txt", "w") as f:
#     f.write("amir")

# if os.path.exists("file_to_delete.txt"):
#     os.remove("file_to_delete.txt")

# ! open("file_to_delete.txt", "r") No such file or directory

# * 3

def research_and_chenge():
    x = input("1::")
    with open("document.txt", "r+", encoding="utf-8") as file, open("uodated_document.txt", "w", encoding="utf-8") as up_f:
        
        a = file.read()
        y = input("2::")
        a.find(x)


research_and_chenge()