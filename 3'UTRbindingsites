#!/usr/bin/env python

from argparse import ArgumentParser

desc = 'Print genes matching a query subsequence'

p = ArgumentParser(description=desc)
p.add_argument('query', help='query subsequence')
p.add_argument('f', help='file containing gene sequences in FASTA format')

a = p.parse_args()

class Gene:
    def __init__(self, name, sequence='AACGGUU'): 
        self.name = name
        self.sequence = sequence
    def message(self,query):
        name = self.name + ': '
        if self.sequence == 'Sequence unavailable':
            return name + 'unavailable'
        i = self.sequence.find(query)
        return name + ('found at position ' + str(i) if i >= 0 else 'not found')

# Create a list of Gene objects from the file
genes = list()
with (open(a.f)) as f:
    for line in f:
        if (line.startswith('>')):
            name = line.split('|')[2][:-1] # remove newline
            genes.append(Gene(name))
        else:
            genes[-1].sequence += line[:-1] # remove newline

for gene in genes:
#    print(gene.name,gene.sequence)
    print(gene.message(a.query))

