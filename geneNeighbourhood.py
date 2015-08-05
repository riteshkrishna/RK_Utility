__author__ = 'riteshk'

'''
    Takes a BED like file with blast hit co-ordinates and looks in a GFF if the blast hists are within the genic region
     or outside. Also if there are any nearby genes annotated. This is specifically for wheat so can be quite messy in
     terms of number of (non)annotations.

     Useful outputs can be - chromosome specific and contig-specific -
     blast hits within genic region -> blast_query - gene name +  blast-location
     non genic hits -> blast_query - nearest gene(if any, blank otherwise) + distance to nearest gene + blast-location

'''

def process_gff(gffFile,blastFile,outFile):
    # relevant gff fields - chr, gene, st, end
    chromosomes = ['1A','1B','1D','2A','2B','2D',
                   '3A','3B','3D','4A','4B','4D',
                   '5A','5B','5D','6A','6B','6D',
                   '7A','7B','7D']
    geneListChrwise = [[] for i in range(21)]
    sorted_geneListChrwise = [[] for i in range(21)]

    non_chr_file = 'non_chr_wheat_file.bed' # Store non-chr genes in this file to save time on parsing GFF every time

    gff_in = open(gffFile)
    nonchr_out = open(non_chr_file,'w')

    for line in gff_in:
        parts = line.split('\t')
        if parts[0] in chromosomes:
            if parts[2] == 'gene':
                attFields = parts[8]
                geneField = attFields.split(';')
                geneID = geneField[0].split('gene:')
                gene_name = geneID[1]
                start = int(parts[3])
                end = int(parts[4])
                chr_index = chromosomes.index(parts[0])
                geneListChrwise[chr_index].append([gene_name,start,end])

    #sorted_by_1 = sorted(geneListChrwise[0], key=lambda tup:tup[1])
    for chr in chromosomes:
        chr_index = chromosomes.index(chr)
        sorted_geneListChrwise[chr_index] = sorted(geneListChrwise[chr_index], key=lambda tup:tup[1])

    #for items in sorted_geneListChrwise:
    #    for genes in items:
    #        print (genes[0] + "\t" + str(genes[1]) + "\t" + str(genes[2]))
    #    print("\n\n")

    blast_in = open(blastFile)
    for line in blast_in:
        parts = line.split("\t")
        query_id = parts[0]
        subject_id = parts[1]
        subject_start = int(parts[8])
        subject_end = int(parts[9])

        if subject_id in chromosomes:
            chr_index = chromosomes.index(subject_id)
            for i in range(len(sorted_geneListChrwise[chr_index])):
                if subject_start <= sorted_geneListChrwise[chr_index][i][2]:
                    if ((subject_end >= sorted_geneListChrwise[chr_index][i-1][1]) and \
                        (subject_end <= sorted_geneListChrwise[chr_index][i-1][2])) or \
                        ((subject_start >= sorted_geneListChrwise[chr_index][i-1][1]) and \
                        (subject_start <= sorted_geneListChrwise[chr_index][i-1][2])) or \
                        ((subject_start >= sorted_geneListChrwise[chr_index][i-1][1]) and \
                        (subject_end <= sorted_geneListChrwise[chr_index][i-1][2])) or \
                        ((subject_start <= sorted_geneListChrwise[chr_index][i-1][1]) and \
                        (subject_end >= sorted_geneListChrwise[chr_index][i-1][2])):
                        #print ("")
                        print ("Overlapping : " + query_id  + "\t" + subject_id  + "\t" + sorted_geneListChrwise[chr_index][i-1][0])
                    else:
                        print ("Non-Overlapping : " + query_id  + "\t" + subject_id  + "\t" + sorted_geneListChrwise[chr_index][i-1][0] + "\t" + sorted_geneListChrwise[chr_index][i][0])

    blast_in.close()
    nonchr_out.close()
    gff_in.close()

if __name__ == "__main__":
    gffFile = 'C:\Ritesh_Work\wheat\Triticum_aestivum.IWGSC1.0_popseq.27.gff3'
    blastFile = 'C:\Ritesh_Work\wheat\out_61_blastn_hits_gt200.txt'
    outFile = 'C:\Ritesh_Work\wheat\pyout.txt'
    process_gff(gffFile,blastFile,outFile)