__author__ = 'riteshk'
'''
    Modify text in an entire column - also across the line for a GFF file
'''
def modify_column(column_number, mod_text,input_file, output_file):

    with open(output_file,mode='w', encoding='utf-8') as out_file:
        with open(input_file,encoding='utf-8') as in_file:
            for line in in_file:
                if line.startswith('##'):
                    out_file.write(line + '\n')
                    continue

                fields = line.split('\t')
                if len(fields) == 9:
                    col_text = fields[column_number]
                    new_text = col_text + '|' + mod_text
                    new_line = line.replace(col_text,new_text)
                    out_file.write(new_line + '\n')
                else :
                    out_file.write(line + '\n')

def read_head(input_file):
    with open(input_file,encoding='utf-8') as in_file:
        counter = 0
        for line in in_file:
            print(line)
            counter += 1
            if counter == 10:
                exit()


if __name__ == "__main__":
    column_number = 0
    mod_text = 'quiver'
    input_file = 'C:\Ritesh_Work\Plutella\maker_px_pacbio_allGff.gff'
    output_file = 'C:\Ritesh_Work\Plutella\mod_maker_px_pacbio_allGff.gff'

    modify_column(column_number,mod_text,input_file,output_file)
    read_head(output_file)



