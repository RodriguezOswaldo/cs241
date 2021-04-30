def prompt_filename():
    file = input('Type in filename: ')
    return file


def look_for_word():
    word = input('Type in the word  you want to look for: ')
    return word


def parse_file(name):
    count = 0
    parsefile = open(name, "r")
    lookup = look_for_word()
    for line in parsefile:
        w = line.split()
        for word in w:
            if word in w:
                word == lookup
                count += 1
            if word == "pride":
                count += 1
        print(line)
    return count


def main():
    file = prompt_filename()
    print(f'The file name is {file}')

    finalcountdown = parse_file(file)

    print(f'The word pride ocurrs {finalcountdown} times in the file.')


if __name__ == '__main__':
    main()
