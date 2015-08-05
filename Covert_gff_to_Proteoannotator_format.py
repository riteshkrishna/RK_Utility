__author__ = 'riteshk'

## Temp program, just for sodalis dataset

def change_gff(gff_file,out_gff):
    f_in = open(gff_file,'r')
    f_out = open(out_gff,'w')

    for line in f_in:
        if line.startswith('##'):
            f_out.write(line)
        elif line.startswith('>'):
            line = line.replace('>','>cds_')
            f_out.write(line)
        elif len(line.split('\t')) == 9:
            fields = line.split('\t')
            print (fields)
            if 'CDS' in fields[2]:
                line = line.replace('ID=','ID=cds_')
                f_out.write(line)
        else:
            f_out.write(line)

    f_in.close()
    f_out.close()


if __name__ == "__main__":
    gff_file = "C:\Ritesh_Work\Sodalis_Data\july6_2015\corr_SgGMM4_final_Ritesh.gff"
    output_file = "C:\Ritesh_Work\Sodalis_Data\july6_2015\PA_SgGMM4_final_Ritesh.gff"
    change_gff(gff_file,output_file)