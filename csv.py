import csv
import os

COVID_DATASET_PATH = os.path.join(
    '.', 'novel-corona-virus-2019-dataset', 'COVID19_open_line_list.csv',
)

def read_dataset_from_csv(csv_path):
    with open(csv_path, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(' | '.join(row))
                line_count += 1
        print(f'Processed {line_count} lines.')


if __name__ == "__main__":
    read_dataset_from_csv(COVID_DATASET_PATH)
