# Copyright (C) 2020, <Justin Villani> <Carlton Semple> -- All Rights Reserved 
# DO NOT REDISTRIBUTE
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential 
# The software MAY NOT be rewritten or refactored by removing the 
# use of LOOP or by the introduction of ITERATE or similar iteration 
# macros with or without prior written permission. The code MAY NOT 
# be packaged and redistributed using the ASDF, ASDF-INSTALL, or 
# QUICKLISP package redistribution tools with or without prior 
# written permission from the author. 
# Subject to the above conditions; and that this COPYRIGHT AND 
# PERMISSION NOTICE appears in ALL copies of the software and 
# supporting documentation or portions thereof, including 
# modifications; and that the name of the author not be used in 
# other form of advertising, merchandise, or publicity pertaining to 
# distribution of the software with or without prior written 
# permission from the author. 

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
