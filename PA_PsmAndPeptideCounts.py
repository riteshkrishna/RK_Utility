__author__ = 'riteshk'

import os

def analyze_exportPSMs_Files(inputdir):

    total_psm = 0
    total_peptides = list()
    unique_peptides = set()

    decoy_col = 17
    pep_col = 10
    psm_col = 4

    for subdir, dirs, files in os.walk(inputdir):
        for file in files:
            correct_psm = 0
            decoy_count = 0
            f_in = open(inputdir+file,'r')

            for line in f_in:
                fields = line.split(',')
                if not 'true' in fields[decoy_col] :
                    correct_psm = correct_psm + 1
                    peptide = fields[pep_col]
                    total_peptides.append(peptide)
                else:
                    decoy_count +=1

            print (file + '\t Decoy count - ' + str(decoy_count) + '\t PSM count - ' + str(correct_psm) + '\t Accum peptides - ' + str(len(total_peptides)) + '\n')
            total_psm = total_psm + correct_psm

            f_in.close()

    unique_peptides = set(total_peptides)
    print ('Total PSMs = ' + str(total_psm) + '\t Total Peptides : ' + str(len(unique_peptides)))


if __name__ == "__main__":
    #csv_dir = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Toxo\\CSVs\\Summary_stats\\PSMCounts\\';
    csv_dir = 'Z:\\Ritesh\\Toxo-version-10\\Results_Sep_2014\\Neo\\Neo_summary_stats\\PSMCounts\\';
    analyze_exportPSMs_Files(csv_dir)