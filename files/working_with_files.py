text_file = open('doc.txt', 'r')

# print(text_file)
# i = 0

# for line in text_file:
#     print(i, line)
#     if i>10:
#         break
#     i += 1

# read file to a limit

print(text_file.readline())
print(text_file.readline(17))

text_file.close()

with open('doc.txt', 'a') as f:
    f.write(f"\n ")