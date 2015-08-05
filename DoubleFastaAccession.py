__author__ = 'riteshk'

# Program to double up FASTA accession

def readFasta(fastaFile,out_fasta):
    f_in = open(fastaFile,'r')
    f_out = open(out_fasta,'w')

    for line in f_in:
        if line.startswith('>'):
            head = line.split()
            replicate = head[0].replace('>','')
            f_out.write(head[0] + ' ' + replicate + '\n')
        else:
            f_out.write(line)

    f_in.close()
    f_out.close()


if __name__ == "__main__":

    fastaFile = "C:\Ritesh_Work\Sodalis_Data\july6_2015\LIV_SODALIS_combined_concatenated_target_decoy.fasta"
    out_fasta = "C:\Ritesh_Work\Sodalis_Data\july6_2015\empai_LIV_SODALIS_combined_concatenated_target_decoy.fasta"
    readFasta(fastaFile,out_fasta)
