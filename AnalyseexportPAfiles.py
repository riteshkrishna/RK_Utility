__author__ = 'riteshk'

def extractRecordsFromGFF(csvFile, gffFile,outfile,label):
    f_in = open(csvFile,'r')
    fout = open(outfile,"a")

    next(f_in) # Skip header

    for line in f_in:
        fields = line.split(',')
        qvalue = float(fields[15])
        #print qvalue
        if qvalue <= float(0.05):
            accession = fields[2]
            if "B_" in accession:
                accession_split = accession.split('B_')
                accession_split_2 = accession_split[1].split("|")
                #to_look_for = 'transcript_id "' + accession_split_2[0]
                to_look_for = accession_split_2[0]
                print('##' + line)
                fout.write('##' + label + '-' +line)
                for gffline in open(gffFile):
                    if to_look_for in gffline:
                        print(gffline)
                        fout.write(gffline)


    f_in.close()
    fout.close()

if __name__ == "__main__":

    csvFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\1DE\\combined_SE_fdr_peptide_threshold_mappedGFF.mzid_proteogrouper.mzid_fdrglobal.mzid_threshold.mzid_non_A.mzid_fdr.mzid.exportProteoAnnotator.csv'
    gffFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\GFF_1DE\\mapped_gff_B.gff'
    outfile = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\all_qval.gff'
    label = '1DE'
    extractRecordsFromGFF(csvFile,gffFile,outfile,label)

    csvFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\2DE\\combined_SE_fdr_peptide_threshold_mappedGFF.mzid_proteogrouper.mzid_fdrglobal.mzid_threshold.mzid_non_A.mzid_fdr.mzid.exportProteoAnnotator.csv'
    gffFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\GFF_2DE\\mapped_gff_B.gff'
    outfile = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\all_qval.gff'
    label = '2DE'
    extractRecordsFromGFF(csvFile,gffFile,outfile,label)

    csvFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\MPIT\\combined_SE_fdr_peptide_threshold_mappedGFF.mzid_proteogrouper.mzid_fdrglobal.mzid_threshold.mzid_non_A.mzid_fdr.mzid.exportProteoAnnotator.csv'
    gffFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\GFF_MPIT\\mapped_gff_B.gff'
    outfile = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\all_qval.gff'
    label = 'MudPIT'
    extractRecordsFromGFF(csvFile,gffFile,outfile,label)

    csvFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\SFIF\\combined_SE_fdr_peptide_threshold_mappedGFF.mzid_proteogrouper.mzid_fdrglobal.mzid_threshold.mzid_non_A.mzid_fdr.mzid.exportProteoAnnotator.csv'
    gffFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\GFF_SFIF\\mapped_gff_B.gff'
    outfile = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\all_qval.gff'
    label = 'SFIF'
    extractRecordsFromGFF(csvFile,gffFile,outfile,label)

    csvFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\Orb_WL\\LIV_ORB1DE_combined_fdr_peptide_threshold_mappedGff_ProteoGrouper_exportProteoAnnotator.csv'
    gffFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\GFF_Orb1WL\\LIV_ORB1DE_me49.new_genes.final_corrected_annotated.gff'
    outfile = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\all_qval.gff'
    label = 'Orb_WL'
    extractRecordsFromGFF(csvFile,gffFile,outfile,label)

    csvFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\Orb-1DE\\LIV_ORB1DE_combined_fdr_peptide_threshold_mappedGff_ProteoGrouper_exportProteoAnnotator.csv'
    gffFile ='Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\GFF_Orb1DE\\LIV_ORB1DE_me49.new_genes.final_corrected_annotated.gff'
    outfile = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\GFFs\\all_qval.gff'
    label = 'Orb_1DE'
    extractRecordsFromGFF(csvFile,gffFile,outfile,label)
