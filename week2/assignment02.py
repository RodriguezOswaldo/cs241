import csv


def prompt_filename():
    return input('Please enter the data file: ')


def parse_file(path):
    # object that holds the records coming from the CSV file
    rates = []
    # read file and append in the object.
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            rates.append(row)
    return rates


def process_file(file):
    """ grab object and process it. """
    result = None
    prom = 0
    lines = 0

    """ dictionary that will hold the four columns I need for both max and min rate. """
    max_rate = {
        'name': None,
        'zip_code': None,
        'state': None,
        'comm_rate': 0
    }
    min_rate = {
        'name': None,
        'zip_code': None,
        'state': None,
        'comm_rate': 1
    }
    # getting the 4 columns from the object
    for row in file:
        comm_rate = float(row[6])
        prom += comm_rate
        lines += 1
        if comm_rate > max_rate['comm_rate']:
            max_rate = {
                'name': row[2],
                'zip_code': row[0],
                'state': row[3],
                'comm_rate': comm_rate
            }

        if comm_rate < min_rate['comm_rate']:
            min_rate = {
                'name': row[2],
                'zip_code': row[0],
                'state': row[3],
                'comm_rate': comm_rate
            }

    result = prom / lines

    max_name = max_rate.get('name')
    max_zip = max_rate.get('zip_code')
    max_st = max_rate.get('state')
    max_code = max_rate.get('comm_rate')
    min_name = min_rate.get('name')
    min_zip = min_rate.get('zip_code')
    min_st = min_rate.get('state')
    min_code = min_rate.get('comm_rate')

    print()
    print(f'The average commercial rate is: {result}')
    print()
    print('The highest rate is:')
    print(f'{max_name} ({max_zip}, {max_st}) - ${max_code}')
    print()
    print('The lowest rate is:')
    print(f'{min_name} ({min_zip}, {min_st}) - ${min_code}')
    return result, max_rate, min_rate

# call the functions


def main():
    # filename = 'rates.csv'
    filename = prompt_filename()
    file = parse_file(filename)
    process_file(file)


if __name__ == '__main__':
    main()
