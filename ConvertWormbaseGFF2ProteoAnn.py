__author__ = 'riteshk'

import fileinput

# ProteoAnnotator has a bug. When the FASTA is included in GFF file, it skips alternate sequences. We insert
# fake sequences before each fasta record to make the FASTA section compatible with PA.
def addFakeSequencesInFastaSection(gff_file, out_gff):

    with open(gff_file, mode = 'r', encoding = 'utf-8') as f_in:
        with open(out_gff, mode = 'w', encoding = 'utf-8') as f_out:

            fake_fasta = '>FAKE_SEQ \n NNNNNNNNNNNNN \n>'

            for line in f_in:
                if line.startswith('>'):
                    f_out.write(line.replace('>',fake_fasta))
                else:
                    f_out.write(line)


# Transdecoder predicted GFF also needs to be converted into PA acceptable format. This code does it.
# Prior to running this code -
# --- run CorrectFastaAccession.py on .pep file to fix the accessions
# --- append ##FASTA and the sequences to the GFF
# --- change >TCONS_ to >rna_ in fasta accessions
# then run this code with the above file as input, to do the following...
# mRNA type will have identifier as ID=rna_xxx and that change will reflect in all parent field where the ID appears.
# FASTA fields will have fake sequences inserted

def fixTransdecoderGffFields(gff_file, out_gff):
    with open(gff_file, mode = 'r', encoding = 'utf-8') as f_in:

        # Create a dictionary of texts to be replaced with new texts
        name_dict = {}

        for line in f_in:
            if len(line.split('\t')) == 9:
                fields = line.split('\t')
                if 'mRNA' in fields[2]:
                    identifier = fields[8].split(';')
                    id_name = identifier[0].split('=')
                    org_name = id_name[1]
                    new_name = org_name.replace('TCONS_','rna_');
                    name_dict[org_name] = new_name


        # Replace the old names with the new names and write in the file
        with open(out_gff, mode = 'w', encoding = 'utf-8') as f_out:
            f_in.seek(0)
            for line in f_in:
                if len(line.split('\t')) == 9:
                    fields = line.split('\t')
                    if 'mRNA' in fields[2]:
                        identifier = fields[8].split(';')
                        id_name = identifier[0].split('=')
                        org_name = id_name[1]
                        new_line = line.replace(org_name, name_dict[org_name])
                        f_out.write(new_line)
                    else:
                        if 'Parent' in fields[8]:
                            identifiers = fields[8].split(';')
                            found = False
                            for identifier in identifiers:
                                if 'Parent' in identifier:
                                    id_name = identifier.split('=')
                                    name = id_name[1].rstrip()
                                    if name in name_dict:
                                        new_line = line.replace(name, name_dict[name])
                                        f_out.write(new_line)
                                        found = True
                                        break
                            if found == False:
                                f_out.write(line)
                        else:
                            f_out.write(line)
                else:
                    f_out.write(line)

            # for key in name_dict:
            #     for line in fileinput.input(gff_file,inplace=True):
            #         print (line.replace(key,name_dict[key]))
            #         #f_out.write(line.replace(key,name_dict[key]))



if __name__ == "__main__":
    # Wormbase file
    #gff_file = "C:/Ritesh_Work/Ochengi/wormbase/PA_onchocerca_volvulus.PRJEB513.WBPS2.annotations_only_WormBase.gff"
    #output_file = "C:/Ritesh_Work/Ochengi/wormbase/FASTA_onchocerca_volvulus.PRJEB513.WBPS2.annotations_only_WormBase.gff"
    #addFakeSequencesInFastaSection(gff_file,output_file)

    # Wormbase file
    gff_file = "C:\Ritesh_Work\Ochengi\PRJEB1809\WormBase_prjeb1809.gff"
    output_file = "C:\Ritesh_Work\Ochengi\PRJEB1809\PA_WormBase_prjeb1809.gff"
    addFakeSequencesInFastaSection(gff_file,output_file)

    ## Transdecoder file
    ## Step 1
    #gff_file = "C:/Ritesh_Work/Ochengi/transdecoder/transcripts.fasta.transdecoder.genome.gff3"
    #output_file = "C:/Ritesh_Work/Ochengi/transdecoder/rnafix_transcripts.fasta.transdecoder.genome.gff3"
    #fixTransdecoderGffFields(gff_file,output_file)
    ## Step 2
    #fas_output_file = "C:/Ritesh_Work/Ochengi/transdecoder/rnafixFastafix_transcripts.fasta.transdecoder.genome.gff3"
    #addFakeSequencesInFastaSection(output_file,fas_output_file)