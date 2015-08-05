__author__ = 'riteshk'

def readFasta(fastaFile,out_fasta):
    f_in = open(fastaFile,'r')
    f_out = open(out_fasta,'w')

    for line in f_in:
        if line.startswith('>'):
            head = line.split()
            f_out.write(head[0] + '\n')
        else:
            f_out.write(line)

    f_in.close()
    f_out.close()


if __name__ == "__main__":
    #fastaFile = "C:/Ritesh_Work/Ochengi/transdecoder/transcripts.fasta.transdecoder.pep"
    #out_fasta = "C:/Ritesh_Work/Ochengi/transdecoder/corr_transcripts.fasta.transdecoder.pep"
    #readFasta(fastaFile,out_fasta)

    #fastaFile = "C:\Ritesh_Work\Ochengi\PRJEB1809\onchocerca_ochengi.PRJEB1809.WBPS2.protein.fa"
    #out_fasta = "C:\Ritesh_Work\Ochengi\PRJEB1809\corr_onchocerca_ochengi.PRJEB1809.WBPS2.protein.fa"
    #readFasta(fastaFile,out_fasta)

    fastaFile = "C:\Ritesh_Work\Sodalis_Data\july6_2015\SgGMM4_final_amino_acids.faa"
    out_fasta = "C:\Ritesh_Work\Sodalis_Data\july6_2015\corr_SgGMM4_final_amino_acids.faa"
    readFasta(fastaFile,out_fasta)
