input_file_path = "macro\\input.cpp"
output_file_path = "macro\\output.cpp"
with open(input_file_path, 'r') as input_file:
    lines = input_file.readlines()
with open(output_file_path, 'w') as output_file:
    a = ""  # varable
    b = ""  # value
    for i in range(len(lines)):
        if "#define" in lines[i]:
            n = i
            a = lines[i][8]
            b = lines[i][10]
        else:
            if a in lines[i]:
                NewLine = ""
                for j in range(len(lines[i])):
                    if lines[i][j] != a:
                        NewLine += lines[i][j]
                    elif lines[i][j] == a:
                        NewLine += b
                output_file.write(NewLine)
            else:
                output_file.write(lines[i])
