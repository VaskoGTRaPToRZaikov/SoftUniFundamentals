path = input().split("\\")

file_name, subtract = path[-1].split(".")

print(f"File name: {file_name}")
print(f"File extension: {subtract}")