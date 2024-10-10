# Get clean id and definition files (erases changes)
git checkout dict/eng-definition.tsv
git checkout data/id-concepticon.tsv
# Run program to append new ids to the id and definition files
python3 src/create_initial_ids_and_definitions.py
# Delete appended ids from the workspace file
#sed -i '/\tready/d' data/id-concepticon-definition.tsv
#sed -i 's/\t$//' data/id-concepticon-definition.tsv
# Sort the id and definition files
gawk -i inplace 'NR<2{print;next}{print|"sort -f"}' data/id-concepticon.tsv
gawk -i inplace 'NR<2{print;next}{print|"sort -f"}' dict/eng-definition.tsv
