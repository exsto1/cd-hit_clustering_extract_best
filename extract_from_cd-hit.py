import re
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-S', help='Minimum cluster size')
parser.add_argument('-C', help='Cluster file')
parser.add_argument('-F', help='Full fasta file')
parser.add_argument('-O', help='Output file template')
parser.add_argument('-N', help='No output clusters. Just full file', action='store_true')

args = parser.parse_args()

start = time.time()
cluster_size = int(args.S)

file = open(args.C).read()
clusters = file.split('>Cluster ')
clusters = [i for i in clusters if i]
counter = 0
sequences_names = {}
for i in range(len(clusters)):
    sequences = clusters[i].split('\n')
    sequences = [i1 for i1 in sequences if i1]
    if len(sequences) > cluster_size:
        sequences_names['Cluster_%s' % sequences[0]] = []
        for i1 in sequences[1:]:
            new_name = re.findall('(>.*?)[...]', i1)
            counter += 1
            sequences_names['Cluster_%s' % sequences[0]].append(new_name[0])


names_full = []
sequences_full = []
seq_temp = ''
all_fastas = open(args.F).readlines()
for i in all_fastas:
    if '>' in i:
        names_full.append(i)
        if seq_temp:
            sequences_full.append(seq_temp)
        seq_temp = ''
    else:
        seq_temp += i
sequences_full.append(seq_temp)


if not args.N:
    zapis_0 = open('%s_save_all.fasta' % args.O, 'w')
    for i in sequences_names:
        zapis_1 = open('%s_%s' % (args.O, i), 'w')
        for i1 in range(len(sequences_names[i])):
            for i2 in range(len(names_full)):
                if sequences_names[i][i1].rstrip() == names_full[i2].rstrip():
                    zapis_0.write(names_full[i2])
                    zapis_0.write(sequences_full[i2])
                    zapis_1.write(names_full[i2])
                    zapis_1.write(sequences_full[i2])
        zapis_1.close()
else:
    zapis_0 = open('%s_save_all.fasta' % args.O, 'w')
    for i in sequences_names:
        for i1 in range(len(sequences_names[i])):
            for i2 in range(len(names_full)):
                if sequences_names[i][i1].rstrip() == names_full[i2].rstrip():
                    zapis_0.write(names_full[i2])
                    zapis_0.write(sequences_full[i2])
zapis_0.close()


print('Minimum cluster size: %s' % cluster_size)
print('%s / %s sequences: %s%%' % (counter, len(names_full), counter * 100/(len(names_full))))
print('Time: %s' % str(time.time() - start))
