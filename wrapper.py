import os

# ---------------------------------------------------------------------------------------------

original_path = './new_cd_hit_all_files/'
original_files = os.listdir(original_path)

cluster_path = './new_cd_hit_all_files/CD50/'
cluster_files = os.listdir(cluster_path)

# ---------------------------------------------------------------------------------------------

for i in original_files:
    for i1 in cluster_files:
        if '.clstr' in i1:
            if i.rstrip('.txt') in i1:
                filename = f'{i.rstrip(".txt")}_50'
                os.system(f'python3 extract_from_cd-hit.py -S 2 -C {cluster_path}{i1} -F {original_path}{i} -O {cluster_path}/extracted_50/{filename} -N')

# ---------------------------------------------------------------------------------------------

extracted_50_path = f'{cluster_path}extracted_50/'
extracted_50 = os.listdir(extracted_50_path)

os.system(f'mkdir {extracted_50_path}CD70')

# ---------------------------------------------------------------------------------------------

for i in extracted_50:
    os.system(f'cdhit -i {extracted_50_path}{i} -o {extracted_50_path}CD70/{i} -c 0.7 -T 1')

# ---------------------------------------------------------------------------------------------

cluster_70_path = f'{extracted_50_path}CD70/'
clusters_70 = os.listdir(cluster_70_path)

os.system(f'mkdir {cluster_70_path}extracted_70')

# ---------------------------------------------------------------------------------------------

for i in original_files:
    for i1 in clusters_70:
        if '.clstr' in i1:
            if i.rstrip('.txt') in i1:
                filename = f'{i.rstrip(".txt")}_70'
                os.system(f'python3 extract_from_cd-hit.py -S 3 -C {cluster_70_path}{i1} -F {original_path}{i} -O {cluster_70_path}extracted_70/{filename} -N')

# ---------------------------------------------------------------------------------------------
