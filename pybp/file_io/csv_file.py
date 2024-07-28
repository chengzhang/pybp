"""load and dump csv file"""

# coding = utf8

import csv


def scan_csv_file(filename, omit_1st_line=False):
    """return a generator of the first field of each line"""
    with open(filename, "r", encoding='utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            # 忽略第一行
            if omit_1st_line and reader.line_num == 1:
                continue
            yield list(row)

def dump_csv_table(table, filename, header=None):
    """table list of list"""
    with open(filename, "w", encoding='utf8', newline='') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        for row in table:
            writer.writerow(row)

def load_csv_table(filename, has_header=False):
    """return the header of csv file, and the content table"""
    header = None
    table = []
    with open(filename, "r", encoding='utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            if has_header and reader.line_num == 1:
                header = list(row)
                continue
            table.append(list(row))
    return header, table
