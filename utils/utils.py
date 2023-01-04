import string
import csv

fields = list()
rows = list()

def read_all_links(alphabet):
    filename = f'./my_files/csv_files/{alphabet}.csv'
    with open(filename, 'r', encoding="utf-8") as file:
        reader = csv.reader(file)
        # Extracting field names through first row
        fields = next(reader)
        # Extracting data from each row one by one
        for row in reader:
            rows.append(row)
        # print("Total no. of rows: %d"%(reader.line_num))
    return rows

def get_count():
    count = 0
    for alphabet in string.ascii_lowercase:
        word_links = read_all_links(alphabet)
        count += len(word_links)
    return count