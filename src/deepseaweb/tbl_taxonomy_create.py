import csv

taxonomy_file='tbl_TAXONOMY.csv'

with open(taxonomy_file.replace('csv','sql') as output_file:
    csv_file = open(taxonomy_file)
    csv_reader = csv.reader(csv.file, delimiter=',')

    for row in csv_reader:
        if csv_reader.line_num == 1:
            csv_reader.next
        else:
            insert_string = "', '".join(row)
            insert_string = "INSERT into tbl_taxonomy VALUES (\'"+insert_string+"\');"
            print >>output_file, insert_string

