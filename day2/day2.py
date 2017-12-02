#!/usr/bin/env python

def main(matrix=None, filename=None, use_division=False):
    if filename is not None:
        matrix = build_matrix(filename)

    if matrix is not None:
        return calculate_checksum(matrix, use_division=use_division)

def calculate_checksum(matrix, use_division=False):
    total = 0
    fn_row_val = get_row_division if use_division else get_row_range
    for row in matrix:
        if row is not []:
            total += fn_row_val(row)
    return total

def get_row_range(row):
    return max(row) - min(row)

def get_row_division(row):
    value = 0
    for x in row:
        for y in row:
            if x > y and x % y == 0:
                value += int(x / y)
    return value

def build_matrix(filename):
    matrix = []
    with open(filename) as f:
        for row in f:
            matrix.append(list(map(int, row.strip().split('\t'))))
    return matrix

if __name__ == "__main__":
    print(main(filename="input.txt", use_division=True))
