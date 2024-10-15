# Get clean id and definition files (erases changes)
git checkout dict/eng-definition.tsv
# Run program to append new ids to the id and definition files
python3 src/write_definition_file.py
# Sort the id and definition files starting from line 2 (i.e. ignore the header line)
gawk -i inplace 'NR<2{print;next}{print|"sort -f"}' dict/eng-definition.tsv
