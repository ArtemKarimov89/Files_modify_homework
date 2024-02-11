file_names = ['1.txt', '2.txt', '3.txt']
file_lists_sorted = []
files_with_data = {}

for file_name in file_names:

    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_lists_sorted.append([file_name, len(lines)])
        files_with_data[file_name] = lines

print(file_lists_sorted)

file_lists_sorted.sort(key=lambda x: x[1])

print(file_lists_sorted)

with open('4.txt', 'w', encoding='utf-8') as f:
    for file in file_lists_sorted:
        file_name = file[0]
        file_len = str(file[1])
        file_data = files_with_data.get(file_name)
        f.write(f'{file_name}\n')
        f.write(f'{file_len}\n')
        for line in file_data:
            f.write(line)
        f.write('\n')




