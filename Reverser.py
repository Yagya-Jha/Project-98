def swapContent():
    f1name = input('Name of File 1: ')
    f2name = input('Name of File 2: ')

    f1 = open(f1name, 'r')
    f2 = open(f2name, 'r')

    data_file_1 = ''
    data_file_2 = ''

    for i in f1:
        data_file_1 = data_file_1 + i

    for j in f2:
        data_file_2 = j

    f1.close()
    f2.close()

    file1 = open(f1name, 'w')
    file2 = open(f2name, 'w')

    file1.write(data_file_2)
    file2.write(data_file_1)

    file1.close()
    file2.close()

swapContent()
close = input('Content of Both mentioned Files Swaped')
