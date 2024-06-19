# 1.11. Copy contents of one file to another line by line

def copy_file(source_file, destination_file):
    with open(source_file, 'r') as f_source, open(destination_file, 'w') as f_dest:
        for line in f_source:
            f_dest.write(line)

source_file = 'demo1.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)


