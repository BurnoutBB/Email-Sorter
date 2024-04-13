print("\033[31m=============================================================================================\033[0m")
ascii_art = '''
\033[31m _______             _ _               ______                               
(_______)           (_) |             / _____)              _               
 _____   ____  _____ _| |    _____   ( (____   ___   ____ _| |_ _____  ____ 
|  ___) |    \(____ | | |   (_____)   \____ \ / _ \ / ___|_   _) ___ |/ ___)
| |_____| | | / ___ | | |             _____) ) |_| | |     | |_| ____| |    
|_______)_|_|_\_____|_|\_)           (______/ \___/|_|      \__)_____)_|    
\033[0m
'''
print(ascii_art)
print("\033[31m=============================================================================================\033[0m")
print()
file_name = input("Enter the file name with emails and passwords (e.g., email_list.txt): ")
print()
print("\033[31m=============================================================================================\033[0m")
print()
domain = input("Enter the email domain you want to filter (e.g., example.com): ")
print()
print("\033[31m=============================================================================================\033[0m")
print()
with open(file_name, 'r') as file:
    lines = file.readlines()
filtered_lines = []
for line in lines:
    if domain in line:
        filtered_lines.append(line)
with open('filtered_list.txt', 'w') as file:
    for line in filtered_lines:
        file.write(line)

print("The list has been filtered successfully. Results saved in 'filtered_list.txt'.")
print()
print("\033[31m=============================================================================================\033[0m")
