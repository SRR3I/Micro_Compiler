with open("input.cpp") as input_file:
    code_cpp = input_file.readlines()
var = ""
val = ""
out_code_cpp = ""
for line in code_cpp:
    if "#define" in line:
        var = line[8]
        val = line[10]
    elif var in line:
        for char in line:
            if var != char:
                out_code_cpp += char
            else:
                out_code_cpp += val
    else:
        out_code_cpp += line

with open("output.cpp", 'w') as output_file:
    output_file.write(out_code_cpp)
