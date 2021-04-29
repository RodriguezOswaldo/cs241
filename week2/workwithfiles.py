users_input = input("Enter file: ")
readfile = open(users_input, "r")
lines = 0
words = 0
for line in readfile:
    line = line.split(" ")
    lines += 1
    for word in line:
        words += 1

print("The file contains " + str(lines) + " lines and " + str(words) + " words.")

readfile.close()
