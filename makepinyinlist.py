import csv
with open('pinyin.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pyset = set()
    for row in csv_reader:
        for cell in row:
            c = str.strip(cell.split(' ')[0])
            if c:
                pyset.add(c)
                pyset.add(c.replace('ü', 'u'))
                pyset.add(c.replace('ü', 'v'))
                pyset.add(c.replace('ê', 'e'))

# with open('pinyin.txt', 'w') as py_file:
#     for py in sorted(pyset):
#         print(py, file=py_file)

print('pylist = [ {} ] '.format(
    ', '.join(["'{}'".format(py) for py in sorted(pyset)])))
