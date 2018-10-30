#from collections import defaultdict


#def count_nucleotides(string):
#    dict = defaultdict(lambda:0)
#    for base in string:
#        dict[base] += 1
#    
#    out = [dict['A'], dict['C'], dict['T'], dict['G']]
#    return " ".join([str(count) for count in out])


def count2(string):
    out = [string.count('A'), string.count('C'), string.count('G'), string.count('T')]
    return " ".join([str(i) for i in out])

if __name__=="__main__":
    print(count2("AGACAGGCGGAACCTTTTGGACACTCGATAACTATATCATGCCGTCCAACCATAGTCACATTTTAGATAAGGAGTTATCAATCGTCACGTAGCACCAATCCGCACGGAGGGTTGATTCCAAACGAGGACTGTGGGAGGCACTAATCTTGTTCGGTCTTAGTAATTGGTCCTTTAACGAACCCTCGCTCGGGCCGTGAAATTTATCCCTCACAATTCTACTCCTTGGGGGCCGGGTACTTCTGAAACGAATTACGCTGGATTGTGCCTCTACTTTGTTGGTTACGCGAAGCAGGGTGGCAATTCAACCCCCACCGACAATGTGTGCCTCTGACATCCATCCGGCCAGTACACTAATACTTAAGCGCCCGAAGTCCATCAGCGCTTGACAGCTCCTGTTCCTGAAAATGCCAGCCGCACAACCGCGGGCTAGGATATCTCGAATGAAACAGAGTGAAAGTTCACAGAAGAAATCCACCTACCAGTAATGAAGACCCCTTCAGACGGGCAGGTGGTTTACCGCAGCTCTAGTACGCTTAGCGGGCGACGTCCTAGTTCTGCTTGAATAGTCGCCACGCGGTTGAGGTTATCCGGGCTAACGGCGTTCAGTCACCCGCCCTGAAGGGGTGGAGGATAATTATCGCTAGGAAAAAACTAACTAGTGTTAGCTGAGGAGAAACCGATGAGATAGGATAGTACCCCAAGACTCCCTCTATTTCGAGAAGAGTGCTGATGTAAGTGTGGTCATGCGTTTGTCCGTTGCAACCGGAATGCGGGCAATCGACTCGATGATGAACAGCGCAAACACGAACCGACGCTTGAAGGAACCACATCATGTCTGGTTTCGCCCACAACTCAAACAGACTGAAAATGTTTTCGGATCTGGGGCTACTCTCCGGTGCGCGCGAGAAAGACAAGCCACCCTGTCAGTTATAACTCACCGTTCAGGTTTTTTATGGGGTTGACGGCGGCTTGTGGAGGGGTTTGCACGGGCAATCTCAA"))

