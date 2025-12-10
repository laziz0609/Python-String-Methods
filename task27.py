file_name = input("File name: ")

result = file_name.endswith(".txt") or file_name.endswith(".docx") or file_name.endswith(".pdf")

print(result)