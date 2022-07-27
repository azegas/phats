# https://www.youtube.com/watch?v=0eCMCk9Bstw

file = open('output/3043210_s4_totxt.txt')
contents = file.read()
# print(contents)
replaced_contents = contents.replace(',', '_')
# print(replaced_contents)

with open('output/3043210_s5_find_replace.txt', "w") as f:
    for i in replaced_contents:
        f.write(i)
