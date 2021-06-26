# educational lvl
import csv


def parse_file(path):
    # object that holds the records coming from the CSV file
    education = {}

    # read file and append in the object.
    with open(path) as f:
        for line in f:
            words = line.split(',')
            word = words[3]
            if word not in education.keys():
                education[word] = 1
            else:
                education[word] += 1

            # if not education.get(word):
            #     education[word] = 1
            # else:
            #     education[word] += 1

            # print(words[3])
    print(education)
    for key, value in education.items():
        print(f'{value} -- {key}')

    # print(education[])

def main():
    path = '/Users/ownos/Programming/cs241/week9/census.csv'
    file = parse_file(path)

    print(file)


if __name__ == "__main__":
    main()