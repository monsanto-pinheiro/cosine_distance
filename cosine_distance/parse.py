'''
Created on Jan 17, 2018

@author: mmp
'''
from BCBio import GFF
from Bio import SeqIO

# $ sudo pip3 install bcbio-gff

if __name__ == '__main__':
	in_file = "/home/mmp/eclipse_oxygen/fluwebvirus/static_all/tests/managing_files/A_H3N2_A_Hong_Kong_4801_2014.gbk"
	out_file = "/tmp/your_file.gff"
	in_handle = open(in_file)
	out_handle = open(out_file, "w")
	
	GFF.write(SeqIO.parse(in_handle, "genbank"), out_handle)
	
	in_handle.close()
	out_handle.close()
	print('finisf')